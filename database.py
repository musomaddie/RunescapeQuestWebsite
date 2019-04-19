import sqlite3
import operator
from passlib.hash import sha256_crypt

MY_DATABASE = "db/quests.db"


class _Vertex_QuestDependencyGraph:
    """ Stores the quest as a vertex in the quest dependency graph
        Parameters:
            quest_name: the name of the quest as it appears in the db
            score: the skill score associated with the given quest
    """
    def __init__(self, quest_name, score):
        self.quest_name = quest_name
        self.score = score
        self.full_processed = False
        self.sub_quests = []


def _calculate_quest_user_skill_distance_score(quest, username):
    distance_score = 0
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute(""" SELECT * FROM user_skills WHERE username=?""",
                (username,))
    user_skills = _get_level_dictionary(cur.fetchone())
    cur.execute(""" SELECT * FROM quest_levels WHERE name=?""",
                (quest,))
    quest_skills = _get_level_dictionary(cur.fetchone())

    for skill in user_skills:
        if user_skills[skill] < quest_skills[skill]:
            distance_score += quest_skills[skill] - user_skills[skill]
    cur.close()
    conn.close()

    return distance_score


def _get_subquests(quest, username, quests_can_complete):
    # NOTE: this recursive approach took far too long to do.
    # Only calculate the next result and save it. Use the result again.
    # Only consider quests that are not complete / cannot be completed

    # yeah this was real dumb. GET THE QUESTS
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute(""" SELECT pre_quest
                    FROM pre_quests
                    WHERE main_quest=?""", (quest,))
    subquests = [x[0] for x in cur.fetchall()]
    cur.close()
    conn.close()
    subquests = list(filter(lambda x: x in subquests, subquests))
    return subquests


def perform_bfs(start_quest, graph):
    visited = [start_quest]
    can_reach = list(filter(lambda x: not x.full_processed,
                            graph[start_quest.quest_name].sub_quests))
    while (can_reach):
        current_quest = can_reach.pop()
        visited.append(current_quest)

        # Update start quest score
        start_quest.score += 10
        start_quest.score += current_quest.score

        # Add it's subquests
        for sq in current_quest.sub_quests:
            if (sq not in visited and
                sq not in can_reach and
                not sq.full_processed):
                can_reach.append(sq)

    start_quest.full_processsed = True


def _calculate_graph_overall_score(graph):
    # TODO: try and speed this up by doing them in heap order with the fewest
    # dependencies being down first. Challenge is will need a fast way to count
    # these. Probably best to have an extra database table and refer to that.
    for quest in graph:
        perform_bfs(graph[quest], graph)
    return graph


def _build_quest_dependency_graph(subquests_by_quest,
                                  quest_scores,
                                  all_quests):
    """ Builds a graph representing the dependencies of all the quests

        Parameters:
            dict<str, list<str>> : a dictionary storing the quest name and a
                list of all the subject quest names

        Returns:
            dict<str, vertex>: a dictionary mapping the quiz name (per db) to
                its vertex representation to easily explore the edges.
    """
    # Add every node as a vertex
    # Only include quests we haven't completed / cannot complete
    graph = {}
    for quest in get_all_quest_names():
        quest = quest[0]
        if quest in all_quests:
            graph[quest] = _Vertex_QuestDependencyGraph(quest,
                                                        quest_scores[quest])
        else:
            graph[quest] = _Vertex_QuestDependencyGraph(quest, 0)

    # Add all the relevant edges -> ignoring quests completed / can complete
    for quest in subquests_by_quest:
        # Ok subquests by quest quest is storing ALL the quests
        for sq in subquests_by_quest[quest]:
            if sq in graph:
                graph[quest].sub_quests.append(graph[sq])

    # Great we have all of this so now we need to actually calculate the score
    # overall
    return _calculate_graph_overall_score(graph)


def _find_quests_almost_available(username):
    """ Return an ordered list of the quests the user is almost able to
        complete by calculating a distance score for each quest and
        choosing the top 10)

        Parameters:
            username(str): the username of the user we are investigating

        Returns:
            list<str>: the name of the top 10 quests they can almost complete
    """
    quests_can_complete = set(_find_quests_can_complete(username))
    # Get all quests not complete
    quest_skill_distance_score = {}
    quest_final_score = {}
    subquests_for_quest = {}
    considered_quests = []
    for quest in get_quests_not_complete(username):
        if quest in quests_can_complete:
            continue
        considered_quests.append(quest)
        quest_skill_distance_score[quest] = _calculate_quest_user_skill_distance_score(quest, username)
        subquests_for_quest[quest] = _get_subquests(quest,
                                                    username,
                                                    quests_can_complete)

    # Let's build the graph for all the quests and then use it.
    quest_graph = _build_quest_dependency_graph(subquests_for_quest,
                                                quest_skill_distance_score,
                                                considered_quests)
    """
    for quest in quest_graph:
        print("Quest: {} score: {}".format(quest, quest_graph[quest].score))
    """
    for quest in considered_quests:
        quest_final_score[quest] = (quest_skill_distance_score[quest]
                                    + quest_graph[quest].score)

    sorted_skills = sorted(quest_final_score.items(),
                           key=operator.itemgetter(1))
    print(sorted_skills)
    return []


def _quests_with_prereqs(username, quests):
    quests_can_complete = []
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute(""" SELECT quest_name
                    FROM user_quests
                    WHERE username=?""", (username,))
    user_quests_complete = set(_fetch_quest_names(cur.fetchall()))

    for quest in quests:
        cur.execute(""" SELECT pre_quest
                        FROM pre_quests
                        WHERE main_quest=?""", (quest,))
        quest_prereq = set(_fetch_quest_names(cur.fetchall()))
        can_do = True
        for q in quest_prereq:
            if q not in user_quests_complete:
                can_do = False
                break
        if can_do:
            quests_can_complete.append(quest)
    cur.close()
    conn.close()
    return quests_can_complete


def _quests_with_levels(username, quests):
    quests_can_complete = []
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute(""" SELECT * FROM user_skills WHERE username=?""",
                (username,))
    user_skills = _get_level_dictionary(cur.fetchone())

    for quest in quests:
        cur.execute(""" SELECT * FROM quest_levels WHERE name=?""",
                    (quest,))
        quest_skills = _get_level_dictionary(cur.fetchone())
        # We are fine to do the following as we know the dictionaries have
        # exactly the same keys
        can_do = True
        for skill in user_skills:
            if user_skills[skill] < quest_skills[skill]:
                can_do = False
                break
        if can_do:
            quests_can_complete.append(quest)

    cur.close()
    conn.close()
    return quests_can_complete


def _find_quests_can_complete(username):
    """ Finds all the quests that the use can currently complete

        Parameters:
            username(str): the username of the user we are investigating

        Returns:
            list<str>: the names of the quests they can complete
    """
    return _quests_with_prereqs(
        username,
        _quests_with_levels(username, get_quests_not_complete(username)))


def _fetch_quest_names(quests):
    """ Retrieves the quest name from the tuple and adds to a new list.

        Parameters:
            quests(list<tuple<str>>): the tuples containing quest names to
                modify.

        Returns:
            list<str>: the list of quest names
    """
    return [x[0] for x in quests]


def _make_dictionary_int(str_dict):
    """ Given a dictionary of keys being strings turns them all into ints """
    new_int_dict = {}
    for key in str_dict:
        try:
            new_int_dict[key] = int(str_dict[key])
        except ValueError:
            continue
    return new_int_dict


def _remove_zero_skills(levels):
    """Given a dict of skills, removes all skills that require level 0 and
    returns the ones remaining.

    Parameters:
        levels (dict<str, int>): the original dictionary containing all the
            skills

    Returns:
        list<tuple<str, int>>: the list of skills and levels, without the 0s
    """
    actual_skills = []
    for skill in levels:
        if levels[skill] != 0:
            actual_skills.append((skill, levels[skill]))
    return actual_skills


def _string_skills(levels):
    """ Given a dictionary of skills, replaces all zeros with an empty string.
        Also makes everything else a string.

        Parameters:
            levels(dict<str, int>): the original dictionary containing all the
            skills.

        Returns:
            dict<str, str>: the new dictionary with everything in strings and
            zero's blanked with empty strings.
    """
    for skill in levels:
        if levels[skill] == 0:
            levels[skill] = ""
        else:
            levels[skill] = str(levels[skill])
    return levels


def _get_level_dictionary(result):
    """
    Given a tuple from the quest_levels or user_skills relation, turns it into
    a dictionary of skill name to associated level.

    Parameters:
        result (tuple): a tuple consisting of one row from the quest_levels
            relation

    Returns:
        dict<str, int>>: each skill mapped to its required level
    """
    return {'Agility': result[1],
            'Attack': result[2],
            'Constitution': result[3],
            'Construction': result[4],
            'Cooking': result[5],
            'Crafting': result[6],
            'Defence': result[7],
            'Divination': result[8],
            'Dungeoneering': result[9],
            'Farming': result[10],
            'Firemaking': result[11],
            'Fishing': result[12],
            'Fletching': result[13],
            'Herblore': result[14],
            'Hunter': result[15],
            'Magic': result[16],
            'Mining': result[17],
            'Prayer': result[18],
            'Ranged': result[19],
            'Runecrafting': result[20],
            'Slayer': result[21],
            'Smithing': result[22],
            'Strength': result[23],
            'Summoning': result[24],
            'Thieving': result[25],
            'Woodcutting': result[26]
            }


def get_all_quest_names():
    """Queries the database for all the quest names

    Returns:
        list<tuple<str>> a list of tuples of which the first (and only) element
            is the name of the quest
    """
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT name FROM quest_details")
    results = cur.fetchall()
    cur.close()
    conn.close()
    if results is None:
        return []
    return results


def get_quest_info(quest_name):
    """ For the quest with the given name, it returns a dictionary of all the
        information.

        Parameters:
            quest_name (str): the name of the quest we are investigating

        Returns:
            dict<str, ?>: a dictionary that maps the name of the quest info to
                its actual info
    """
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()

    cur.execute(""" SELECT * FROM quest_details WHERE name=?""",
                (quest_name,))
    results_details = cur.fetchone()

    cur.execute(""" SELECT * FROM quest_levels WHERE name=?""",
                (quest_name,))
    result_levels = _remove_zero_skills(_get_level_dictionary(cur.fetchone()))

    cur.execute(""" SELECT pre_quest FROM pre_quests WHERE main_quest=?""",
                (quest_name, ))
    result_pre_quests = [x[0] for x in cur.fetchall()]
    result_pre_quests.sort()

    cur.execute(""" SELECT requirement
                    FROM quest_other_requirements
                    WHERE name=?""", (quest_name,))
    result_other_requirements = [x[0] for x in cur.fetchall()]

    cur.execute(""" SELECT name
                    FROM quest_series
                    WHERE quest=?""", (quest_name, ))
    result_quest_series = [x[0] for x in cur.fetchall()]

    cur.execute(""" SELECT name
                    FROM quest_series_related
                    WHERE quest=?""", (quest_name,))
    result_quest_series_related = [x[0] for x in cur.fetchall()]

    # Make this all into a dictionary so we can refer to it easily inside the
    # HTML
    final_result = {"name": results_details[0],
                    "free?": "yes" if results_details[1] else "no",
                    "age": results_details[2],
                    "difficulty": results_details[3],
                    "length": results_details[4],
                    "quest points": results_details[5],
                    "skills": result_levels,
                    "pre quests": result_pre_quests,
                    "other requirements": result_other_requirements,
                    "quest series": result_quest_series,
                    "related quests": result_quest_series_related
                    }

    cur.close()
    conn.close()
    return final_result


def _get_quest_info_recursive(quest_name, parent_quest, all_quests):
    """ A recursive helper method for get_quest_info_including_sub. Will
        process everything including subquests correctly.

        Parameters:
            quest_name(str): the name of the quest
            parent_quest(str): the quest that this is a parent of.
            all_quests(list<dict<str, dict<str, str>>>): the list of all quests
            processed this far.

        Returns:
            None: as the list is modified in place
    """
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()

    cur.execute(""" SELECT * FROM quest_levels WHERE name=?""", (quest_name,))
    skills = _string_skills(_get_level_dictionary(cur.fetchone()))
    this_quest_skills_info = skills

    cur.execute(""" SELECT requirement
                    FROM quest_other_requirements
                    WHERE name=?""", (quest_name,))
    other_requirements = [x[0] for x in cur.fetchall()]
    this_quest_skills_info["other requirements"] = other_requirements
    this_quest_skills_info["name"] = quest_name
    this_quest_skills_info["parent quest"] = parent_quest

    all_quests.append(this_quest_skills_info)
    # TODO: update return types to match this in documentation

    cur.execute(""" SELECT pre_quest FROM pre_quests WHERE main_quest=?""",
                (quest_name, ))
    sub_quests = [x[0] for x in cur.fetchall()]
    cur.close()
    conn.close()

    for quest in sub_quests:
        _get_quest_info_recursive(quest, quest_name, all_quests)


def get_quest_info_including_sub(quest_name):
    """ For the quest with the given name return its level as well as the
        levels for all its subquests.

        Parameters:
            quest_name(str): the name of the quest we are investigating

        Returns:
            list<dict<str, dict<str, str>>>: a list where each item corresponds
                to a particular quest (in subquest order). This is a dictionary
                containing the quest name, mapped to the levels, parent quest
                and other requirements for that quest.


    """
    all_quests = []
    parent_quest = None
    _get_quest_info_recursive(quest_name, parent_quest, all_quests)
    return all_quests


def add_new_user(username, password):
    """ Adds a new user to the database.

        Parameters:
            username(str): The username to register
            password(str): The already hashed and salted password associated
                with the username.

        Returns:
            bool: True if the user was added successfully, false if there was
                an error.
    """
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    try:
        cur.execute(""" INSERT INTO username_password VALUES(
                            ?, ?);
                    """, (username, password))
    except Exception:
        return False

    # If this was successfully added we need to add a row to user_skills to
    # allow display even if the user has not added any skills
    cur.execute(""" INSERT INTO user_skills VALUES(
        ?, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0); """, (username,))
    conn.commit()
    cur.close()
    conn.close()
    return True


def login(username, password):
    """ Attempts to log in an existing user.

        Parameters:
            username(str): the username of the user that wishes to login.
            password(str): the non salted and hashed password of the user

        Returns:
            list<bool, opt<str>>: the boolean contains whether the login was
                successful and the str explains why not (if applicable)
    """
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute(""" SELECT password
                    FROM username_password
                    WHERE username=?""",
                (username,))
    encrypted_password = cur.fetchone()
    cur.close()
    conn.close()
    if encrypted_password is None:
        return [False, "No user with that username exists"]
    password_match = sha256_crypt.verify(password, encrypted_password[0])
    if not password_match:
        return [False, "Incorrect username or password"]
    return [True]


def get_user_profile(username):
    """ Retrieves all the details that are needed to display a user profile

        Parameters:
            username(str): the username of the profile to display

        Returns:
            dict<str: str>: maps the type of information to its actual value
    """
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute(""" SELECT * FROM user_skills WHERE username=?""",
                (username,))
    user_dict = _get_level_dictionary(cur.fetchone())
    user_dict["name"] = username
    cur.execute(""" SELECT quest_name
                    FROM user_quests
                    WHERE username=? """,
                (username, ))
    user_dict["Quests"] = _fetch_quest_names(cur.fetchall())
    user_dict["quests can complete"] = _find_quests_can_complete(username)
    user_dict["quests almost available"] = _find_quests_almost_available(
        username)
    cur.close()
    conn.close()
    return user_dict


def update_user_skills(username, skills_to_update_str_dict):
    """ Updates all the skill levels for the given user.

        Parameters:
            username(str): the user to update skills for
            skills_to_update_str_dict(dict<str: str>): the dictionary
                containing the updated skill values

        Returns:
            tuple(boolean, optional error message): if this process succeeded
                returns (true) otherwise returns (false, error)
    """
    skills_to_update = _make_dictionary_int(skills_to_update_str_dict)
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute("""UPDATE user_skills
                   SET
                        agility=?,
                        attack=?,
                        constitution=?,
                        construction=?,
                        cooking=?,
                        crafting=?,
                        defence=?,
                        divination=?,
                        dungeoneering=?,
                        farming=?,
                        firemaking=?,
                        fishing=?,
                        fletching=?,
                        herblore=?,
                        hunter=?,
                        magic=?,
                        mining=?,
                        prayer=?,
                        ranged=?,
                        runecrafting=?,
                        slayer=?,
                        smithing=?,
                        strength=?,
                        summoning=?,
                        thieving=?,
                        woodcutting=?
                    WHERE username=?;
                """, (
                      skills_to_update["agility"],
                      skills_to_update["attack"],
                      skills_to_update["constitution"],
                      skills_to_update["construction"],
                      skills_to_update["cooking"],
                      skills_to_update["crafting"],
                      skills_to_update["defence"],
                      skills_to_update["divination"],
                      skills_to_update["dungeoneering"],
                      skills_to_update["farming"],
                      skills_to_update["firemaking"],
                      skills_to_update["fishing"],
                      skills_to_update["fletching"],
                      skills_to_update["herblore"],
                      skills_to_update["hunter"],
                      skills_to_update["magic"],
                      skills_to_update["mining"],
                      skills_to_update["prayer"],
                      skills_to_update["ranged"],
                      skills_to_update["runecrafting"],
                      skills_to_update["slayer"],
                      skills_to_update["smithing"],
                      skills_to_update["strength"],
                      skills_to_update["summoning"],
                      skills_to_update["thieving"],
                      skills_to_update["woodcutting"],
                      username
                      ))
    conn.commit()
    cur.close()
    conn.close()
    return [True]


def get_quests_not_complete(username):
    """ Returns all the quest names the user HAS NOT completed

        Parameters:
            username(str): the user we are investigating

        Returns:
            list<str>: the list of quest names
    """
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute(""" SELECT name
                        FROM quest_details
                EXCEPT
                    SELECT quest_name
                        FROM user_quests
                        WHERE username=? ; """, (username,))
    all_matching_quests = _fetch_quest_names(cur.fetchall())
    cur.close()
    conn.close()
    return all_matching_quests


def add_quest_to_user(username, questname):
    """ Adds the given quest to the given users completed quests

        Parameters:
            username(str): the user who completed the quest
            quest(str): the quest that was completed

        Returns:
            list<bool, str>: if the quest was added successfully, true if it
                was and false with an error message otherwise
    """
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute(""" SELECT name FROM quest_details WHERE name=?""",
                (questname, ))
    if not cur.fetchone():
        return [False, "{} does not exist!".format(questname)]
    cur.execute(""" SELECT quest_name
                    FROM user_quests
                    WHERE username=? AND quest_name=?""",
                (username, questname))
    if cur.fetchone():
        return [False, "You have already completed {}".format(questname)]

    cur.execute(""" INSERT INTO user_quests VALUES(?, ?); """,
                (username, questname))
    conn.commit()
    cur.close()
    conn.close()

    return [True]
