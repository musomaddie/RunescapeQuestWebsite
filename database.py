import sqlite3


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
    conn = sqlite3.connect("db/quests.db")
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
    conn = sqlite3.connect("db/quests.db")
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
