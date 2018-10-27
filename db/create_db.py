import os
import sys
import sqlite3

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("db")])

from QuestSetUp import create_all_quests


def populate_db(db):
    quests = create_all_quests()
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    for quest in quests:
        cur.execute("""
                    INSERT INTO quest_details VALUES(
                        ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?, ?, ?);
        """, (quest.name,
              quest.free,
              quest.age,
              quest.difficulty,
              quest.length,
              quest.quest_points,
              quest.agility,
              quest.attack,
              quest.constitution,
              quest.construction,
              quest.cooking,
              quest.crafting,
              quest.defence,
              quest.divination,
              quest.dungeoneering,
              quest.farming,
              quest.firemaking,
              quest.fishing,
              quest.fletching,
              quest.herblore,
              quest.hunter,
              quest.magic,
              quest.mining,
              quest.prayer,
              quest.ranged,
              quest.runecrafting,
              quest.slayer,
              quest.smithing,
              quest.strength,
              quest.summoning,
              quest.thieving,
              quest.woodcutting)
        )

    conn.commit()

    cur.close()
    conn.close()


def init_db(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS quest_details""")

    # Set up table of quest details
    cur.execute('''
                CREATE TABLE quest_details (
                    name TEXT PRIMARY KEY,
                    is_free BOOLEAN NOT NULL,
                    age INTEGER NOT NULL,
                    difficulty TEXT NOT NULL,
                    length TEXT NOT NULL,
                    quest_points INTEGER NOT NULL,
                    agility INTEGER,
                    attack INTEGER,
                    constitution INTEGER,
                    construction INTEGER,
                    cooking INTEGER,
                    crafting INTEGER,
                    defence INTEGER,
                    divination INTEGER,
                    dungeoneering INTEGER,
                    farming INTEGER,
                    firemaking INTEGER,
                    fishing INTEGER,
                    fletching INTEGER,
                    herblore INTEGER,
                    hunter INTEGER,
                    magic INTEGER,
                    mining INTEGER,
                    prayer INTEGER,
                    ranged INTEGER,
                    runecrafting INTEGER,
                    slayer INTEGER,
                    smithing INTEGER,
                    strength INTEGER,
                    summoning INTEGER,
                    thieving INTEGER,
                    woodcutting INTEGER
                );
            ''')
    conn.commit()
    cur.close()
    conn.close()

    # Set up table containing other requirements


if __name__ == '__main__':
    init_db('quests.db')
    populate_db('quests.db')
