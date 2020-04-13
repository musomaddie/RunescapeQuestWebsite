import os
import sys
import sqlite3

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quest_map")])

from quest_map.GridCell import GridCell
from quest_map.GridQuest import GridQuest

MAPPING_HEIGHT = 84
MAPPING_WIDTH = 14
# TODO: the database name does depend on where you run it, currently cant run
#  from inside the folder
DATABASE_NAME = "db/quests.db"


def calculate_quest_positions(mapping, all_quests, quests_relations):

    def add_to_mapping(quest_list, x, y):
        for q in quest_list:
            if q is not None:
                gq = GridQuest(q, (x, y))
                quests_relations[q] = gq
                mapping[y][x].add_quest(gq)
                # print("Q: {} AQ: {}".format(q, all_quests[q]))
            y += 1

    order_of_quests = ["Sheep Herder", "Mountain Daughter",
                       "Tears of Guthix (quest)", "Cook's Assistant",
                       "Hazeel Cult", "The Blood Pact",
                       "Horror from the Deep", "Rune Mechanics",
                       "Rune Mysteries",
                       "The Hand in the Sand", "Tribal Totem",
                       "The Fremennik Trials", "Murder Mystery", "Plague City",
                       "Big Chompy Bird Hunting", "Eagles' Peak",
                       "Jungle Potion", "Merlin's Crystal", "Dragon Slayer",
                       "Druidic Ritual", "Lost City", "Shield of Arrav",
                       "Death Plateau", "The Feud", "The Golem",
                       "Demon Slayer",
                       "Pirate's Treasure", "Family Crest",
                       "The Knight's Sword", "What Lies Below",
                       "Waterfall Quest", "Temple of Ikov",
                       "Shades of Mort'ton", "The Tale of the Muspah",
                       "The Dig Site", "The Tourist Trap", "Priest in Peril",
                       "Spirits of the Elid", "The Restless Ghost",
                       "Ernest the Chicken", "What's Mine is Yours",
                       "Imp Catcher", "Recruitment Drive", "Goblin Diplomacy",
                       "Stolen Hearts", "Gertrude's Cat", "Cold War",
                       "Sea Slug", "Tree Gnome Village", "The Grand Tree",
                       "Fishing Contest", "Dwarf Cannon", "The Giant Dwarf",
                       "Witch's House", "Watchtower",
                       "Enakhra's Lament", "Fight Arena",
                       "The Firemaker's Curse", "The Death of Chivalry",
                       "Elemental Workshop I",
                       "Rag and Bone Man", "Bringing Home the Bacon",
                       "Beneath Cursed Tides", "Clock Tower",
                       "Call of the Ancestors", "Buyers and Cellars",
                       "Broken Home", "Gunnar's Ground", "In Pyre Need",
                       "Let Them Eat Pie", "Wolf Whistle", "Monk's Friend",
                       "Myths of the White Lands", "Observatory Quest",
                       "One Piercing Note", "Perils of Ice Mountain",
                       "Enlightened Journey", "Gower Quest",
                       "Song from the Depths", "A Soul's Bane", "Swept Away",
                       "TokTz-Ket-Dill", "Vampyre Slayer", "Violet is Blue"
                       ]
    add_to_mapping(order_of_quests, 0, 0)

    second_order_of_quests = [
        "Chef's Assistant", "Carnillean Rising", None, None, None,
        "Rune Memories", None, "The Fremennik Isles", "Olaf's Quest", None,
        "Biohazard", "Zogre Flesh Eaters", "Tai Bwo Wannai Trio",
        "Shilo Village", "Holy Grail", None, "Heroes' Quest", None, None,
        "Troll Stronghold", "Shadow of the Storm", None, None, None,
        None, None, None, None, None, None, "All Fired Up",
        "Ghosts Ahoy", "Nature Spirit", "Creature of Fenkenstrain",
        "Making History", "Animal Magnetism", "Spirit of Summer", None,
        "The Lost Tribe", "Diamond in the Rough", None, None,
        "Hunt for Red Raktuber", None, "Monkey Madness",
        "The Eyes of Glouphrie",
        "Between a Rock...", "Forgettable Tale of a Drunken Dwarf",
        "Grim Tales", None, None, None, None, None, "Elemental Workshop II",
        "Fur 'n Seek"
    ]
    add_to_mapping(second_order_of_quests, 1, 3)

    third_order_quests = ["Heart of Stone", None, None, None,
                          "Throne of Miscellania", "Underground Pass",
                          "As a First Resort", None, "One Small Favour",
                          None, None, None, "Lunar Diplomacy",
                          None, "Eadgar's Ruse", "Troll Romance", None, None,
                          "A Fairy Tale I - Growing Pains", None, "Rum Deal",
                          None, None, "Desert Treasure", None, None, None,
                          None, "In Search of the Myreque", "Haunted Mine",
                          "Garden of Tranquillity", "Meeting History",
                          "Wanted!", "Summer's End", "Death to the Dorgeshuun",
                          "Icthlarin's Little Helper", "The Jack of Spades",
                          None, "Some Like It Cold", None,
                          "The Path of Glouphrie", None, None,
                          "Forgiveness of a Chaos Dwarf", None, None, None,
                          None, None, None, "Elemental Workshop III"
                          ]
    add_to_mapping(third_order_quests, 2, 8)

    fourth_order_quests = ["Royal Trouble", "Regicide", None,
                           "Back to my Roots", "King's Ransom", None, None,
                           "Hero's Welcome", "Legends' Quest", "Dream Mentor",
                           "My Arm's Big Adventure", "Swan Song", None,
                           "A Fairy Tale II - Cure a Queen", None,
                           "Cabin Fever", None, "Defender of Varrock", None,
                           None, None, None, None, "In Aid of the Myreque",
                           None, None, "Devious Minds", "Missing My Mummy",
                           "Quiet Before the Swarm", "Another Slice of H.A.M.",
                           "Contact!", "Rat Catchers", "Smoking Kills",
                           "A Tail of Two Cats", "Back to the Freezer",
                           "The Slug Menace", None, None, None, None, None,
                           None, None, None, None, None,
                           "Elemental Workshop IV"
                           ]
    add_to_mapping(fourth_order_quests, 3, 12)

    fifth_order_quests = ["Glorious Memories", "Roving Elves",
                          "Catapult Construction", None, None,
                          "Nomad's Requiem", None, None, None, None, None,
                          None, None,
                          "A Fairy Tale III - Battle at Ork's Rift", None,
                          None, "While Guthix Sleeps", None,
                          "The Curse of Arrav",
                          None, None, None, None, "The Darkness of Hallowvale",
                          None, "Recipe for Disaster", None, None,
                          "A Void Dance", "Land of the Goblins", None,
                          "Dealing with Scabaras", None, None, None,
                          "Kennith's Concerns", None, "King of the Dwarves",
                          ]
    add_to_mapping(fifth_order_quests, 4, 12)

    sixth_order_quests1 = ["Blood Runs Deep", "Mourning's End Part I"]
    add_to_mapping(sixth_order_quests1, 5, 12)

    sixth_order_quests2 = ["The Temple at Senntisten", "Love Story",
                           "Dimension of Disaster", None, None,
                           "Legacy of Seergaze", "Do No Evil",
                           "Evil Dave's Big Day Out",
                           "The Great Brain Robbery",
                           "Crocodile Tears", None, "The Void Stares Back",
                           "The Chosen Commander", None, None,
                           "The Prisoner of Glouphrie", None,
                           "Salt in the Wound", None,
                           "Birthright of the Dwarves"]
    add_to_mapping(sixth_order_quests2, 5, 28)

    seventh_order_quests1 = ["Mourning's End Part II"]
    add_to_mapping(seventh_order_quests1, 6, 14)
    add_to_mapping(["Within the Light"], 7, 15)
    add_to_mapping(["Plague's End"], 8, 17)

    seventh_order_quests2 = ["The Branches of Darkmeyer", None,
                             "Our Man in the North", None, "Rocking Out",
                             ]
    add_to_mapping(seventh_order_quests2, 6, 34)

    eighth_order_quests = ["The Lord of Vampyrium", None, "'Phite Club", None,
                           "Ritual of the Mahjarrat", None,
                           "A Clockwork Syringe"
                           ]
    add_to_mapping(eighth_order_quests, 7, 33)

    ninth_order_quests = ["River of Blood", None, None, None,
                          "The World Wakes", "Pieces of Hate"]
    add_to_mapping(ninth_order_quests, 8, 34)

    add_to_mapping(["Missing, Presumed Death"], 9, 37)
    eleventh_order = ["Dishonour among Thieves", "One of a Kind",
                      "Fate of the Gods", "The Mighty Fall", "Kindred Spirits"
                      ]
    add_to_mapping(eleventh_order, 10, 36)
    add_to_mapping(["The Light Within", None, "Nomad's Elegy"], 11, 37)
    add_to_mapping(["Children of Mah"], 12,  37)
    add_to_mapping(["Sliske's Endgame"], 13, 38)

    # All all the quests to the relations mapping
    for quest in quests_relations:
        for nextquest in all_quests[quest]:
            try:
                quests_relations[quest].required_for.append(
                    quests_relations[nextquest])
            except KeyError:
                print("{} doesn't exist".format(nextquest))


def get_all_quests():
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    cur.execute(""" SELECT name, required_quest
                    FROM quest_details LEFT OUTER JOIN required_quests
                    ON (name = main_quest)
                ;""")
    results = cur.fetchall()
    cur.close()
    conn.close()
    quests_and_reqs = {key: [] for key in
                       set([r[0] for r in results])}
    for result in results:
        quest, required_quest = result
        if required_quest is not None:
            quests_and_reqs[required_quest].append(quest)
    return quests_and_reqs


def calculate_arrow(original_quest, parent_quest, cell_mapping):
    orig_x, orig_y = original_quest.position
    par_x, par_y = parent_quest.position
    horizontal_distance = original_quest.horizontal_difference(
        parent_quest)
    # Saving vertical difference as a variable to save soo much typing
    # this is positive if parent is higher, negative otherwise
    vertical_difference = original_quest.vertical_difference(parent_quest)
    # Returns true if the orig quest is in an even layer
    is_orig_even_layer = orig_x % 2 == 0
    is_par_imm_below = (vertical_difference == 0 if is_orig_even_layer else
                        vertical_difference == 1)
    is_par_imm_above = (vertical_difference == -1 if is_orig_even_layer else
                        vertical_difference == 0)
    is_par_diag_below = (vertical_difference == 1 if is_orig_even_layer else
                         vertical_difference == 2)
    is_par_diag_above = (vertical_difference == -2 if is_orig_even_layer else
                         vertical_difference == -1)
    is_par_far_below = vertical_difference > 1
    is_par_far_above = vertical_difference < -1

    def calc_exit_point():
        # Returns true if the whole arrow has been calculated
        # TODO: neaten this part!
        # If it's far away =
        if horizontal_distance > 1:
            cell_mapping[orig_y][orig_x].add_exit_point(2)
            return False

        if is_par_imm_below:
            cell_mapping[orig_y][orig_x].add_exit_point(3)
            cell_mapping[par_y][par_x].add_entry_point(1)
            return True
        if is_par_imm_above:
            cell_mapping[orig_y][orig_x].add_exit_point(1)
            cell_mapping[par_y][par_x].add_entry_point(3)
            return True
        if is_par_diag_below:
            cell_mapping[orig_y][orig_x].add_exit_point(4)
            return False
        if is_par_diag_above:
            cell_mapping[orig_y][orig_x].add_exit_point(0)
            return False
        # Order matters (otherwise far will count when it's not meant too
        if is_par_far_below:
            cell_mapping[orig_y][orig_x].add_exit_point(4)
        if is_par_far_above:
            cell_mapping[orig_y][orig_x].add_exit_point(0)

    def calc_entry_point():
        # If the exit and entry points are the same it won't reach here
        if horizontal_distance > 1:
            # TODO: deal with this!!
            return
        if is_par_diag_below:
            cell_mapping[par_y][par_x].add_entry_point(0)
        if is_par_diag_above:
            cell_mapping[par_y][par_x].add_entry_point(4)
        # Again order matters:
        if is_par_far_below:
            cell_mapping[par_y][par_x].add_entry_point(0)
        if is_par_far_above:
            cell_mapping[par_y][par_x].add_entry_point(4)

    # Find the exit point
    if calc_exit_point():
        # If returns true, nothing more to calculate
        return

    # Find the middle flow
        # Heads Right
        # Heads Down

    # Find the entry point
    calc_entry_point()


def create_initial_mapping():
    mapping = [[GridCell((i, j)) for i in range(MAPPING_WIDTH)]
               for j in range(MAPPING_HEIGHT)]
    # Remember when indexing it's y x
    all_quests = get_all_quests()
    all_quests_relations = {}
    # Some comments explaining wtf this is would help :)
    calculate_quest_positions(mapping, all_quests, all_quests_relations)
    # TODO: make the arrows!
    for q in all_quests_relations:
        for rq in all_quests_relations[q].required_for:
            calculate_arrow(all_quests_relations[q], rq, mapping)
        x, y = all_quests_relations[q].position


if __name__ == '__main__':
    create_initial_mapping()
