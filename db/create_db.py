import os
import sys
import sqlite3

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("db")])

from quests.quest_scraping import load_all_quests

DB_NAME = "quests.db"


def populate_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    quests = load_all_quests()
    for quest in quests:
        cur.execute('''
                    INSERT INTO quest_details
                    VALUES (?, ?, ?, ?, ?, 0);
                    ''',
                    (quests[quest].name,
                     quests[quest].is_free,
                     quests[quest].age,
                     quests[quest].difficulty,
                     quests[quest].length))
        cur.execute('''
                    INSERT INTO quest_levels
                    VALUES (?, ?, ?, ?, ?, ?,
                            ?, ?, ?, ?, ?,
                            ?, ?, ?, ?, ?,
                            ?, ?, ?, ?, ?,
                            ?, ?, ?, ?, ?, ?);
                    ''',
                    (quests[quest].name,
                     quests[quest].agility,
                     quests[quest].attack,
                     quests[quest].constitution,
                     quests[quest].construction,
                     quests[quest].cooking,
                     quests[quest].crafting,
                     quests[quest].defence,
                     quests[quest].divination,
                     quests[quest].dungeoneering,
                     quests[quest].farming,
                     quests[quest].firemaking,
                     quests[quest].fishing,
                     quests[quest].fletching,
                     quests[quest].herblore,
                     quests[quest].hunter,
                     quests[quest].magic,
                     quests[quest].mining,
                     quests[quest].prayer,
                     quests[quest].ranged,
                     quests[quest].runecrafting,
                     quests[quest].slayer,
                     quests[quest].smithing,
                     quests[quest].strength,
                     quests[quest].summoning,
                     quests[quest].thieving,
                     quests[quest].woodcutting))
    for quest in quests.values():
        for prequest in quest.pre_quests:
            cur.execute('''
                        INSERT INTO required_quests
                        VALUES (?, ?); ''',
                        (quest.name, prequest))
    conn.commit()
    cur.close()
    conn.close()


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS quest_details""")
    cur.execute("""DROP TABLE IF EXISTS quest_levels""")
    cur.execute("""DROP TABLE IF EXISTS required_quests""")
    cur.execute("""DROP TABLE IF EXISTS quest_other_requirements""")
    cur.execute("""DROP TABLE IF EXISTS quest_series""")
    cur.execute("""DROP TABLE IF EXISTS quest_series_related""")
    cur.execute("""DROP TABLE IF EXISTS username_password""")
    cur.execute("""DROP TABLE IF EXISTS user_skills""")
    cur.execute("""DROP TABLE IF EXISTS user_quests""")

    cur.execute('''
                CREATE TABLE quest_details (
                    name TEXT PRIMARY KEY,
                    is_free BOOLEAN NOT NULL,
                    age INTEGER NOT NULL,
                    difficulty TEXT NOT NULL,
                    length TEXT NOT NULL,
                    quest_points INTEGER NOT NULL
                );
            ''')

    cur.execute('''
                CREATE TABLE quest_levels(
                    name TEXT PRIMARY KEY,
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
                    woodcutting INTEGER,
                    FOREIGN KEY (name) REFERENCES quest_details(name)
                );
            ''')

    cur.execute('''
                CREATE TABLE required_quests(
                    main_quest TEXT,
                    required_quest TEXT,
                    PRIMARY KEY (main_quest, required_quest)
                    FOREIGN KEY (main_quest) REFERENCES quest_details (name),
                    FOREIGN KEY (required_quest)
                            REFERENCES quest_details (name)
                );
                ''')

    cur.execute('''
                CREATE TABLE quest_other_requirements(
                    name TEXT,
                    requirement TEXT,
                    PRIMARY KEY (name, requirement)
                    FOREIGN KEY (name) REFERENCES quest_details(name)
                );
                ''')

    cur.execute('''
                CREATE TABLE quest_series(
                    name TEXT,
                    quest TEXT,
                    number INTEGER,
                    PRIMARY KEY (name, quest)
                    FOREIGN KEY (quest) REFERENCES quest_details(name)
                );
                ''')

    cur.execute('''
                CREATE TABLE quest_series_related(
                    name TEXT,
                    quest TEXT,
                    PRIMARY KEY (name, quest)
                    FOREIGN KEY (quest) REFERENCES quest_details(name)
                );
                ''')

    cur.execute('''
                CREATE TABLE username_password(
                    username TEXT,
                    password TEXT,
                    PRIMARY KEY(username)
                );
                ''')
    cur.execute('''
                CREATE TABLE user_skills(
                    username TEXT PRIMARY KEY,
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
                    woodcutting INTEGER,
                FOREIGN KEY (username) REFERENCES username_password(username)
                );
            ''')

    cur.execute('''
                CREATE TABLE user_quests(
                    username TEXT,
                    quest_name TEXT,
                    PRIMARY KEY(username, quest_name),
                FOREIGN KEY (username) REFERENCES username_password(username),
                    FOREIGN KEY (quest_name) REFERENCES quest_details(name)
                );
                ''')

    conn.commit()
    cur.close()
    conn.close()

    # Set up table containing other requirements


if __name__ == '__main__':
    init_db()
    populate_db()
