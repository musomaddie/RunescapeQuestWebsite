import sqlite3


def remove_zero_skills(levels):
    actual_skills = []
    for skill in levels:
        if levels[skill] != 0:
            actual_skills.append((skill, levels[skill]))
    return actual_skills


def get_level_dictionary(result):
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
    conn = sqlite3.connect("db/quests.db")
    cur = conn.cursor()
    cur.execute(""" SELECT * FROM quest_details WHERE name=?""",
                (quest_name,))
    results_details = cur.fetchone()
    cur.execute(""" SELECT * FROM quest_levels WHERE name=?""",
                (quest_name,))
    result_levels = remove_zero_skills(get_level_dictionary(cur.fetchone()))
    print(result_levels)
    cur.execute(""" SELECT requirement
                    FROM quest_other_requirements
                    WHERE name=?""", (quest_name,))
    result_other_requirements = [x[0] for x in cur.fetchall()]
    print(result_other_requirements)
    # Make this all into a dictionary so we can refer to it easily inside the
    # HTML

    final_result = {"name": results_details[0],
                    }

    cur.close()
    conn.close()
    return final_result
