import sqlite3


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
    results1 = cur.fetchone()
    # Need to do something to leave us with only the remaining skills.
    # Could maybe rework the database and split skills up so that I can get the
    # skills separately to the rest of the data easily?
    cur.close()
    conn.close()
    return results1
