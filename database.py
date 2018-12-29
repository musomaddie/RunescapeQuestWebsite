import sqlite3

MY_DATABASE = "db/quests.db"


def remove_zero_skills(levels):
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


def string_skills(levels):
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


def get_level_dictionary(result):
    """
    Given a tuple from the quest_levels relation, turn it into a dictionary
    of skill name to required level.

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
    result_levels = remove_zero_skills(get_level_dictionary(cur.fetchone()))

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


def get_quest_info_recursive(quest_name, parent_quest, all_quests):
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
    skills = string_skills(get_level_dictionary(cur.fetchone()))
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
        get_quest_info_recursive(quest, quest_name, all_quests)


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
    get_quest_info_recursive(quest_name, parent_quest, all_quests)
    return all_quests


def get_all_free_or_members_quests(free):
    """ Get all the quest names where they are either paid or free

        Parameters:
            free(bool): whether or not the quest is available to free players
                or not.

        Returns:
            list<tuple<str>>: a list of tuples where the first and only element
                is the name of the quest.
    """

    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    is_free = False
    if free == "yes":
        is_free = True
    cur.execute("""SELECT name FROM quest_details WHERE is_free=?""",
                (is_free,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    if results is None:
        return []
    return results
