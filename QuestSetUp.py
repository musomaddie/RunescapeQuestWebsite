import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("")])
from quests.All_Fired_Up import All_Fired_Up
from quests.Animal_Magnetism import Animal_Magnetism
from quests.Another_Slice_Of_Ham import Another_Slice_Of_Ham
from quests.As_A_First_Resort import As_A_First_Resort
from quests.Back_To_My_Roots import Back_To_My_Roots
from quests.Back_To_The_Freezer import Back_To_The_Freezer
from quests.Beneath_Cursed_Tides import Beneath_Cursed_Tides
from quests.Between_A_Rock import Between_A_Rock
from quests.Big_Chompy_Bird_Hunting import Big_Chompy_Bird_Hunting
from quests.Biohazard import Biohazard
from quests.Birthright_Of_The_Dwarves import Birthright_Of_The_Dwarves
from quests.The_Blood_Pact import The_Blood_Pact
from quests.Blood_Runs_Deep import Blood_Runs_Deep
from quests.The_Branches_Of_Darkmeyer import The_Branches_Of_Darkmeyer
from quests.Bringing_Home_The_Bacon import Bringing_Home_The_Bacon
from quests.The_Brink_Of_Extinction import The_Brink_Of_Extinction
from quests.Broken_Home import Broken_Home
from quests.Buyers_And_Cellars import Buyers_And_Cellars
from quests.Cabin_Fever import Cabin_Fever
from quests.Call_Of_The_Ancestors import Call_Of_The_Ancestors
from quests.Carnillean_Rising import Carnillean_Rising
from quests.Catapult_Construction import Catapult_Construction
from quests.Children_Of_Mah import Children_Of_Mah
from quests.The_Chosen_Commander import The_Chosen_Commander
from quests.Clock_Tower import Clock_Tower
from quests.A_Clockwork_Syringe import A_Clockwork_Syringe
from quests.Cold_War import Cold_War
from quests.Contact import Contact
from quests.Cooks_Assistant import Cooks_Assistant
from quests.Creature_Of_Fenkenstrain import Creature_Of_Fenkenstrain
from quests.Crocodile_Tears import Crocodile_Tears
from quests.The_Curse_Of_Arrav import The_Curse_Of_Arrav
from quests.Darkness_Of_Hallowvale import Darkness_Of_Hallowvale
from quests.Deadliest_Catch import Deadliest_Catch
from quests.Dealing_With_Scabaras import Dealing_With_Scabaras
from quests.The_Death_Of_Chivalry import The_Death_Of_Chivalry
from quests.Death_To_The_Dorgeshuun import Death_To_The_Dorgeshuun
from quests.Death_Plateau import Death_Plateau
from quests.Defender_Of_Varrock import Defender_Of_Varrock
from quests.Demon_Slayer import Demon_Slayer
from quests.Desert_Treasure import Desert_Treasure
from quests.Devious_Minds import Devious_Minds
from quests.Diamond_In_The_Rough import Diamond_In_The_Rough
from quests.The_Dig_Site import The_Dig_Site
from quests.Dimension_Of_Disaster import Dimension_Of_Disaster
from quests.Dishonour_Among_Thieves import Dishonour_Among_Thieves
from quests.Do_No_Evil import Do_No_Evil
from quests.Dragon_Slayer import Dragon_Slayer
from quests.Dream_Mentor import Dream_Mentor
from quests.Druidic_Ritual import Druidic_Ritual
from quests.Dwarf_Cannon import Dwarf_Cannon
from quests.Eadgars_Ruse import Eadgars_Ruse
from quests.Eagles_Peak import Eagles_Peak
from quests.The_Elder_Kiln import The_Elder_Kiln
from quests.Elemental_Workshop_I import Elemental_Workshop_I
from quests.Elemental_Workshop_II import Elemental_Workshop_II
from quests.Elemental_Workshop_III import Elemental_Workshop_III
from quests.Elemental_Workshop_IV import Elemental_Workshop_IV
from quests.Enakhras_Lament import Enakhras_Lament
from quests.Enlightened_Journey import Enlightened_Journey
from quests.Ernest_The_Chicken import Ernest_The_Chicken
from quests.Evil_Daves_Big_Day_Out import Evil_Daves_Big_Day_Out
from quests.The_Eyes_Of_Glouphrie import The_Eyes_Of_Glouphrie
from quests.Fairy_Tale_I_Growing_Pains import Fairy_Tale_I_Growing_Pains
from quests.Fairy_Tale_II_Cure_A_Queen import Fairy_Tale_II_Cure_A_Queen
from quests.Fairy_Tale_III_Battle_At_Orks_Rift import Fairy_Tale_III_Battle_At_Orks_Rift
from quests.Family_Crest import Family_Crest
from quests.Fate_Of_The_Gods import Fate_Of_The_Gods
from quests.The_Feud import The_Feud
from quests.Fight_Arena import Fight_Arena
from quests.The_Firemakers_Curse import The_Firemakers_Curse
from quests.Fishing_Contest import Fishing_Contest
from quests.Forgettable_Tale import Forgettable_Tale
from quests.Forgiveness_Of_A_Chaos_Dwarf import Forgiveness_Of_A_Chaos_Dwarf
from quests.The_Fremennik_Isles import The_Fremennik_Isles
from quests.The_Fremennik_Trials import The_Fremennik_Trials
from quests.Fur_N_Seek import Fur_N_Seek
from quests.Garden_Of_Tranquillity import Garden_Of_Tranquillity
from quests.Gertrudes_Cat import Gertrudes_Cat
from quests.Ghosts_Ahoy import Ghosts_Ahoy
from quests.The_Giant_Dwarf import The_Giant_Dwarf
from quests.Glorious_Memories import Glorious_Memories
from quests.Goblin_Diplomacy import Goblin_Diplomacy
from quests.The_Golem import The_Golem
from quests.Gower_Quest import Gower_Quest
from quests.The_Grand_Tree import The_Grand_Tree
from quests.The_Great_Brain_Robbery import The_Great_Brain_Robbery
from quests.Gunnars_Ground import Gunnars_Ground
from quests.Grim_Tales import Grim_Tales
from quests.The_Hand_In_The_Sand import The_Hand_In_The_Sand
from quests.Haunted_Mine import Haunted_Mine
from quests.Hazeel_Cult import Hazeel_Cult
from quests.Heart_Of_Stone import Heart_Of_Stone
from quests.Heros_Welcome import Heros_Welcome
from quests.Heroes_Quest import Heroes_Quest
from quests.Holy_Grail import Holy_Grail
from quests.Horror_From_The_Deep import Horror_From_The_Deep
from quests.Hunt_For_Red_Raktuber import Hunt_For_Red_Raktuber
from quests.Icthlarins_Little_Helper import Icthlarins_Little_Helper
from quests.Imp_Catcher import Imp_Catcher
from quests.Impressing_The_Locals import Impressing_The_Locals
from quests.In_Aid_Of_The_Myreque import In_Aid_Of_The_Myreque
from quests.In_Pyre_Need import In_Pyre_Need
from quests.In_Search_Of_The_Myreque import In_Search_Of_The_Myreque
from quests.The_Jack_Of_Spades import The_Jack_Of_Spades
from quests.Jungle_Potion import Jungle_Potion
from quests.Kenniths_Concerns import Kenniths_Concerns
from quests.Kindred_Spirits import Kindred_Spirits
from quests.King_Of_The_Dwarves import King_Of_The_Dwarves
from quests.Kings_Ransom import Kings_Ransom
from quests.The_Knights_Sword import The_Knights_Sword
from quests.Land_Of_The_Goblins import Land_Of_The_Goblins
from quests.Legacy_Of_Seergaze import Legacy_Of_Seergaze
from quests.Legends_Quest import Legends_Quest
from quests.Let_Them_Eat_Pie import Let_Them_Eat_Pie
from quests.The_Light_Within import The_Light_Within
from quests.The_Lord_Of_Vampyrium import The_Lord_Of_Vampyrium
from quests.Lost_City import Lost_City
from quests.The_Lost_Tribe import The_Lost_Tribe
from quests.Love_Story import Love_Story
from quests.Lunar_Diplomacy import Lunar_Diplomacy
from quests.Making_History import Making_History
from quests.Meeting_History import Meeting_History
from quests.Merlins_Crystal import Merlins_Crystal
from quests.The_Mighty_Fall import The_Mighty_Fall
from quests.Missing_My_Mummy import Missing_My_Mummy
from quests.Missing_Presumed_Death import Missing_Presumed_Death
from quests.Monkey_Madness import Monkey_Madness
from quests.Monks_Friend import Monks_Friend
from quests.Mountain_Daughter import Mountain_Daughter
from quests.Mournings_End_Part_I import Mournings_End_Part_I
from quests.Mournings_End_Part_II import Mournings_End_Part_II
from quests.Murder_Mystery import Murder_Mystery
from quests.My_Arms_Big_Adventure import My_Arms_Big_Adventure
from quests.Myths_Of_The_White_Lands import Myths_Of_The_White_Lands
from quests.Nature_Spirit import Nature_Spirit
from quests.Nomads_Elegy import Nomads_Elegy
from quests.Nomads_Requiem import Nomads_Requiem
from quests.Observatory_Quest import Observatory_Quest
from quests.Olafs_Quest import Olafs_Quest
from quests.One_Of_A_Kind import One_Of_A_Kind
from quests.One_Piercing_Note import One_Piercing_Note
from quests.One_Small_Favour import One_Small_Favour
from quests.Our_Man_In_The_North import Our_Man_In_The_North
from quests.The_Path_Of_Glouphrie import The_Path_Of_Glouphrie
from quests.Phite_Club import Phite_Club
from quests.Perils_Of_Ice_Mountain import Perils_Of_Ice_Mountain
from quests.Pieces_Of_Hate import Pieces_Of_Hate
from quests.Pirates_Treasure import Pirates_Treasure
from quests.Plague_City import Plague_City
from quests.Plagues_End import Plagues_End
from quests.Priest_In_Peril import Priest_In_Peril
from quests.The_Prisoner_Of_Glouphrie import The_Prisoner_Of_Glouphrie
from quests.Quiet_Before_The_Swarm import Quiet_Before_The_Swarm
from quests.Rag_And_Bone_Man import Rag_And_Bone_Man
from quests.Ratcatchers import Ratcatchers
from quests.Recipe_For_Disaster import Recipe_For_Disaster
from quests.Recruitment_Drive import Recruitment_Drive
from quests.Regicide import Regicide
from quests.The_Restless_Ghost import The_Restless_Ghost
from quests.Ritual_Of_The_Mahjarrat import Ritual_Of_The_Mahjarrat
from quests.River_Of_Blood import River_Of_Blood
from quests.Rocking_Out import Rocking_Out
from quests.Roving_Elves import Roving_Elves
from quests.Royal_Trouble import Royal_Trouble
from quests.Rum_Deal import Rum_Deal
from quests.Rune_Mechanics import Rune_Mechanics
from quests.Rune_Memories import Rune_Memories
from quests.Rune_Mysteries import Rune_Mysteries
from quests.Salt_In_The_Wound import Salt_In_The_Wound
from quests.Scorpion_Catcher import Scorpion_Catcher
from quests.Sea_Slug import Sea_Slug
from quests.Shades_Of_Mortton import Shades_Of_Mortton
from quests.A_Shadow_Over_Ashdale import A_Shadow_Over_Ashdale
from quests.Shadow_Of_The_Storm import Shadow_Of_The_Storm
from quests.Sheep_Herder import Sheep_Herder
from quests.Shield_Of_Arrav import Shield_Of_Arrav
from quests.Shilo_Village import Shilo_Village
from quests.Sliskes_Endgame import Sliskes_Endgame
from quests.The_Slug_Menace import The_Slug_Menace
from quests.Smoking_Kills import Smoking_Kills
from quests.Some_Like_It_Cold import Some_Like_It_Cold
from quests.Song_From_The_Depths import Song_From_The_Depths
from quests.A_Souls_Bane import A_Souls_Bane
from quests.Spirit_Of_Summer import Spirit_Of_Summer
from quests.Spirits_Of_The_Elid import Spirits_Of_The_Elid
from quests.Stolen_Hearts import Stolen_Hearts
from quests.Summers_End import Summers_End
from quests.Swan_Song import Swan_Song
from quests.Swept_Away import Swept_Away
from quests.Tai_Bwo_Wannai_Trio import Tai_Bwo_Wannai_Trio
from quests.A_Tail_Of_Two_Cats import A_Tail_Of_Two_Cats
from quests.The_Tale_Of_The_Muspah import The_Tale_Of_The_Muspah
from quests.Tears_Of_Guthix import Tears_Of_Guthix
from quests.The_Temple_At_Senntisten import The_Temple_At_Senntisten
from quests.Temple_Of_Ikov import Temple_Of_Ikov
from quests.Throne_Of_Miscellania import Throne_Of_Miscellania
from quests.The_Tourist_Trap import The_Tourist_Trap
from quests.Tower_Of_Life import Tower_Of_Life
from quests.TokTz_Ket_Dill import TokTz_Ket_Dill
from quests.Tree_Gnome_Village import Tree_Gnome_Village
from quests.Tribal_Totem import Tribal_Totem
from quests.Troll_Romance import Troll_Romance
from quests.Troll_Stronghold import Troll_Stronghold
from quests.Underground_Pass import Underground_Pass
from quests.Vampyre_Slayer import Vampyre_Slayer
from quests.A_Void_Dance import A_Void_Dance
from quests.The_Void_Stares_Back import The_Void_Stares_Back
from quests.Wanted import Wanted
from quests.WatchTower import WatchTower
from quests.Waterfall_Quest import Waterfall_Quest
from quests.What_Lies_Below import What_Lies_Below
from quests.Whats_Mine_Is_Yours import Whats_Mine_Is_Yours
from quests.While_Guthix_Sleeps import While_Guthix_Sleeps
from quests.Witchs_House import Witchs_House
from quests.Within_The_Light import Within_The_Light
from quests.Wolf_Whistle import Wolf_Whistle
from quests.The_World_Wakes import The_World_Wakes


def create_all_quests():

    all_fired_up = All_Fired_Up()
    animal_magnetism = Animal_Magnetism()
    another_slice_of_ham = Another_Slice_Of_Ham()
    as_a_first_resort = As_A_First_Resort()

    back_to_my_roots = Back_To_My_Roots()
    back_to_the_freezer = Back_To_The_Freezer()
    between_a_rock = Between_A_Rock()
    beneath_cursed_tides = Beneath_Cursed_Tides()
    big_chompy_bird_hunting = Big_Chompy_Bird_Hunting()
    biohazard = Biohazard()
    birthright_of_the_dwarves = Birthright_Of_The_Dwarves()
    the_blood_pact = The_Blood_Pact()
    blood_runs_deep = Blood_Runs_Deep()
    the_branches_of_darkmeyer = The_Branches_Of_Darkmeyer()
    bringing_home_the_bacon = Bringing_Home_The_Bacon()
    the_brink_of_extinction = The_Brink_Of_Extinction()
    broken_home = Broken_Home()
    buyers_and_cellars = Buyers_And_Cellars()

    cabin_fever = Cabin_Fever()
    call_of_the_ancestors = Call_Of_The_Ancestors()
    carnillean_rising = Carnillean_Rising()
    catapult_construction = Catapult_Construction()
    children_of_mah = Children_Of_Mah()
    the_chosen_commander = The_Chosen_Commander()
    clock_tower = Clock_Tower()
    a_clockwork_syringe = A_Clockwork_Syringe()
    cold_war = Cold_War()
    contact = Contact()
    cooks_assistant = Cooks_Assistant()
    creature_of_fenkenstrain = Creature_Of_Fenkenstrain()
    crocodile_tears = Crocodile_Tears()
    the_curse_of_arrav = The_Curse_Of_Arrav()

    darkness_of_hallowvale = Darkness_Of_Hallowvale()
    deadliest_catch = Deadliest_Catch()
    dealing_with_scabaras = Dealing_With_Scabaras()
    the_death_of_chivalry = The_Death_Of_Chivalry()
    death_to_the_dorgeshuun = Death_To_The_Dorgeshuun()
    death_plateau = Death_Plateau()
    defender_of_varrock = Defender_Of_Varrock()
    demon_slayer = Demon_Slayer()
    desert_treasure = Desert_Treasure()
    devious_minds = Devious_Minds()
    diamond_in_the_rough = Diamond_In_The_Rough()
    the_dig_site = The_Dig_Site()
    dimension_of_disaster = Dimension_Of_Disaster()
    dishonour_among_thieves = Dishonour_Among_Thieves()
    do_no_evil = Do_No_Evil()
    dragon_slayer = Dragon_Slayer()
    dream_mentor = Dream_Mentor()
    druidic_ritual = Druidic_Ritual()
    dwarf_cannon = Dwarf_Cannon()

    eadgars_ruse = Eadgars_Ruse()
    eagles_peak = Eagles_Peak()
    the_elder_kiln = The_Elder_Kiln()
    elemental_workshop_i = Elemental_Workshop_I()
    elemental_workshop_ii = Elemental_Workshop_II()
    elemental_workshop_iii = Elemental_Workshop_III()
    elemental_workshop_iv = Elemental_Workshop_IV()
    enakhras_lament = Enakhras_Lament()
    enlightened_journey = Enlightened_Journey()
    ernest_the_chicken = Ernest_The_Chicken()
    evil_daves_big_day_out = Evil_Daves_Big_Day_Out()
    the_eyes_of_glouphrie = The_Eyes_Of_Glouphrie()

    fairy_tale_i_growing_pains = Fairy_Tale_I_Growing_Pains()
    fairy_tale_ii_cure_a_queen = Fairy_Tale_II_Cure_A_Queen()
    fairy_tale_iii_battle_at_orks_rift = Fairy_Tale_III_Battle_At_Orks_Rift()
    family_crest = Family_Crest()
    fate_of_the_gods = Fate_Of_The_Gods()
    the_feud = The_Feud()
    fight_arena = Fight_Arena()
    the_firemakers_curse = The_Firemakers_Curse()
    fishing_contest = Fishing_Contest()
    forgettable_tale = Forgettable_Tale()
    forgiveness_of_a_chaos_dwarf = Forgiveness_Of_A_Chaos_Dwarf()
    the_fremennik_isles = The_Fremennik_Isles()
    the_fremennik_trials = The_Fremennik_Trials()
    fur_n_seek = Fur_N_Seek()

    garden_of_tranquillity = Garden_Of_Tranquillity()
    gertrudes_cat = Gertrudes_Cat()
    ghosts_ahoy = Ghosts_Ahoy()
    the_giant_dwarf = The_Giant_Dwarf()
    glorious_memories = Glorious_Memories()
    goblin_diplomacy = Goblin_Diplomacy()
    the_golem = The_Golem()
    gower_quest = Gower_Quest()
    the_grand_tree = The_Grand_Tree()
    the_great_brain_robbery = The_Great_Brain_Robbery()
    grim_tales = Grim_Tales()
    gunnars_ground = Gunnars_Ground()

    the_hand_in_the_sand = The_Hand_In_The_Sand()
    haunted_mine = Haunted_Mine()
    hazeel_cult = Hazeel_Cult()
    heart_of_stone = Heart_Of_Stone()
    heros_welcome = Heros_Welcome()
    heroes_quest = Heroes_Quest()
    holy_grail = Holy_Grail()
    horror_from_the_deep = Horror_From_The_Deep()
    hunt_for_red_raktuber = Hunt_For_Red_Raktuber()

    imp_catcher = Imp_Catcher()
    icthlarins_little_helper = Icthlarins_Little_Helper()
    impressing_the_locals = Impressing_The_Locals()
    in_aid_of_the_myreque = In_Aid_Of_The_Myreque()
    in_pyre_need = In_Pyre_Need()
    in_search_of_the_myreque = In_Search_Of_The_Myreque()

    the_jack_of_spades = The_Jack_Of_Spades()
    jungle_potion = Jungle_Potion()

    kenniths_concerns = Kenniths_Concerns()
    kindred_spirits = Kindred_Spirits()
    king_of_the_dwarves = King_Of_The_Dwarves()
    kings_ransom = Kings_Ransom()
    the_knights_sword = The_Knights_Sword()

    land_of_the_goblins = Land_Of_The_Goblins()
    legacy_of_seergaze = Legacy_Of_Seergaze()
    legends_quest = Legends_Quest()
    let_them_eat_pie = Let_Them_Eat_Pie()
    the_light_within = The_Light_Within()
    the_lord_of_vampyrium = The_Lord_Of_Vampyrium()
    lost_city = Lost_City()
    the_lost_tribe = The_Lost_Tribe()
    love_story = Love_Story()
    lunar_diplomacy = Lunar_Diplomacy()

    making_history = Making_History()
    meeting_history = Meeting_History()
    merlins_crystal = Merlins_Crystal()
    the_mighty_fall = The_Mighty_Fall()
    missing_my_mummy = Missing_My_Mummy()
    missing_presumed_death = Missing_Presumed_Death()
    monkey_madness = Monkey_Madness()
    monks_friend = Monks_Friend()
    mountain_daughter = Mountain_Daughter()
    mournings_end_part_i = Mournings_End_Part_I()
    mournings_end_part_ii = Mournings_End_Part_II()
    murder_mystery = Murder_Mystery()
    my_arms_big_adventure = My_Arms_Big_Adventure()
    myths_of_the_white_lands = Myths_Of_The_White_Lands()

    nature_spirit = Nature_Spirit()
    nomads_elegy = Nomads_Elegy()
    nomads_requiem = Nomads_Requiem()

    observatory_quest = Observatory_Quest()
    olafs_quest = Olafs_Quest()
    one_of_a_kind = One_Of_A_Kind()
    one_piercing_note = One_Piercing_Note()
    one_small_favour = One_Small_Favour()
    our_man_in_the_north = Our_Man_In_The_North()

    the_path_of_glouphrie = The_Path_Of_Glouphrie()
    phite_club = Phite_Club()
    perils_of_ice_mountain = Perils_Of_Ice_Mountain()
    pieces_of_hate = Pieces_Of_Hate()
    pirates_treasure = Pirates_Treasure()
    plague_city = Plague_City()
    plagues_end = Plagues_End()
    priest_in_peril = Priest_In_Peril()
    the_prisoner_of_glouphrie = The_Prisoner_Of_Glouphrie()

    quiet_before_the_swarm = Quiet_Before_The_Swarm()

    rag_and_bone_man = Rag_And_Bone_Man()
    ratcatchers = Ratcatchers()
    recipe_for_disaster = Recipe_For_Disaster()
    recruitment_drive = Recruitment_Drive()
    regicide = Regicide()
    the_restless_ghost = The_Restless_Ghost()
    ritual_of_the_mahjarrat = Ritual_Of_The_Mahjarrat()
    river_of_blood = River_Of_Blood()
    rocking_out = Rocking_Out()
    roving_elves = Roving_Elves()
    royal_trouble = Royal_Trouble()
    rum_deal = Rum_Deal()
    rune_mechanics = Rune_Mechanics()
    rune_memories = Rune_Memories()
    rune_mysteries = Rune_Mysteries()

    salt_in_the_wound = Salt_In_The_Wound()
    scorpion_catcher = Scorpion_Catcher()
    sea_slug = Sea_Slug()
    shades_of_mortton = Shades_Of_Mortton()
    a_shadow_over_ashdale = A_Shadow_Over_Ashdale()
    shadow_of_the_storm = Shadow_Of_The_Storm()
    shield_of_arrav = Shield_Of_Arrav()
    sheep_herder = Sheep_Herder()
    shilo_village = Shilo_Village()
    sliskes_endgame = Sliskes_Endgame()
    the_slug_menace = The_Slug_Menace()
    smoking_kills = Smoking_Kills()
    some_like_it_cold = Some_Like_It_Cold()
    song_from_the_depths = Song_From_The_Depths()
    a_souls_bane = A_Souls_Bane()
    spirit_of_summer = Spirit_Of_Summer()
    spirits_of_the_elid = Spirits_Of_The_Elid()
    stolen_hearts = Stolen_Hearts()
    summers_end = Summers_End()
    swan_song = Swan_Song()
    swept_away = Swept_Away()

    tai_bwo_wannai_trio = Tai_Bwo_Wannai_Trio()
    a_tail_of_two_cats = A_Tail_Of_Two_Cats()
    the_tale_of_the_muspah = The_Tale_Of_The_Muspah()
    tears_of_guthix = Tears_Of_Guthix()
    the_temple_at_senntisten = The_Temple_At_Senntisten()
    temple_of_ikov = Temple_Of_Ikov()
    throne_of_miscellania = Throne_Of_Miscellania()
    toktz_ket_dill = TokTz_Ket_Dill()
    the_tourist_trap = The_Tourist_Trap()
    tower_of_life = Tower_Of_Life()
    tree_gnome_village = Tree_Gnome_Village()
    tribal_totem = Tribal_Totem()
    troll_romance = Troll_Romance()
    troll_stronghold = Troll_Stronghold()

    underground_pass = Underground_Pass()

    vampyre_slayer = Vampyre_Slayer()
    a_void_dance = A_Void_Dance()
    the_void_stares_back = The_Void_Stares_Back()

    wanted = Wanted()
    watchtower = WatchTower()
    waterfall_quest = Waterfall_Quest()
    what_lies_below = What_Lies_Below()
    whats_mine_is_yours = Whats_Mine_Is_Yours()
    while_guthix_sleeps = While_Guthix_Sleeps()
    witchs_house = Witchs_House()
    within_the_light = Within_The_Light()
    wolf_whistle = Wolf_Whistle()
    the_world_wakes = The_World_Wakes()

    all_quests = [beneath_cursed_tides,
                  the_blood_pact,
                  broken_home,
                  cooks_assistant,
                  the_death_of_chivalry,
                  death_plateau,
                  demon_slayer,
                  dragon_slayer,
                  druidic_ritual,
                  ernest_the_chicken,
                  gertrudes_cat,
                  goblin_diplomacy,
                  gower_quest,
                  gunnars_ground,
                  imp_catcher,
                  the_knights_sword,
                  let_them_eat_pie,
                  missing_presumed_death,
                  myths_of_the_white_lands,
                  one_piercing_note,
                  perils_of_ice_mountain,
                  priest_in_peril,
                  the_restless_ghost,
                  rune_mysteries,
                  a_shadow_over_ashdale,
                  shield_of_arrav,
                  song_from_the_depths,
                  a_souls_bane,
                  stolen_hearts,
                  swept_away,
                  vampyre_slayer,
                  whats_mine_is_yours,
                  witchs_house,
                  wolf_whistle,
                  all_fired_up,
                  another_slice_of_ham,
                  animal_magnetism,
                  as_a_first_resort,
                  back_to_my_roots,
                  back_to_the_freezer,
                  between_a_rock,
                  big_chompy_bird_hunting,
                  biohazard,
                  pirates_treasure,
                  birthright_of_the_dwarves,
                  blood_runs_deep,
                  the_branches_of_darkmeyer,
                  bringing_home_the_bacon,
                  the_brink_of_extinction,
                  buyers_and_cellars,
                  cabin_fever,
                  call_of_the_ancestors,
                  carnillean_rising,
                  catapult_construction,
                  children_of_mah,
                  the_chosen_commander,
                  clock_tower,
                  a_clockwork_syringe,
                  cold_war,
                  contact,
                  creature_of_fenkenstrain,
                  crocodile_tears,
                  the_curse_of_arrav,
                  darkness_of_hallowvale,
                  deadliest_catch,
                  dealing_with_scabaras,
                  death_to_the_dorgeshuun,
                  defender_of_varrock,
                  desert_treasure,
                  devious_minds,
                  diamond_in_the_rough,
                  the_dig_site,
                  dimension_of_disaster,
                  dishonour_among_thieves,
                  do_no_evil,
                  dream_mentor,
                  dwarf_cannon,
                  eadgars_ruse,
                  eagles_peak,
                  the_elder_kiln,
                  elemental_workshop_i,
                  elemental_workshop_ii,
                  elemental_workshop_iii,
                  elemental_workshop_iv,
                  enakhras_lament,
                  enlightened_journey,
                  evil_daves_big_day_out,
                  the_eyes_of_glouphrie,
                  fairy_tale_i_growing_pains,
                  fairy_tale_ii_cure_a_queen,
                  fairy_tale_iii_battle_at_orks_rift,
                  family_crest,
                  fate_of_the_gods,
                  the_feud,
                  fight_arena,
                  the_firemakers_curse,
                  fishing_contest,
                  forgettable_tale,
                  forgiveness_of_a_chaos_dwarf,
                  the_fremennik_isles,
                  the_fremennik_trials,
                  fur_n_seek,
                  garden_of_tranquillity,
                  ghosts_ahoy,
                  the_giant_dwarf,
                  glorious_memories,
                  the_golem,
                  the_grand_tree,
                  the_great_brain_robbery,
                  grim_tales,
                  the_hand_in_the_sand,
                  haunted_mine,
                  hazeel_cult,
                  heart_of_stone,
                  heros_welcome,
                  heroes_quest,
                  holy_grail,
                  horror_from_the_deep,
                  hunt_for_red_raktuber,
                  icthlarins_little_helper,
                  impressing_the_locals,
                  in_aid_of_the_myreque,
                  in_pyre_need,
                  in_search_of_the_myreque,
                  the_jack_of_spades,
                  jungle_potion,
                  kenniths_concerns,
                  kindred_spirits,
                  king_of_the_dwarves,
                  kings_ransom,
                  land_of_the_goblins,
                  legacy_of_seergaze,
                  legends_quest,
                  the_light_within,
                  the_lord_of_vampyrium,
                  lost_city,
                  the_lost_tribe,
                  love_story,
                  lunar_diplomacy,
                  making_history,
                  meeting_history,
                  merlins_crystal,
                  the_mighty_fall,
                  missing_my_mummy,
                  monks_friend,
                  monkey_madness,
                  mountain_daughter,
                  mournings_end_part_i,
                  mournings_end_part_ii,
                  murder_mystery,
                  my_arms_big_adventure,
                  nature_spirit,
                  nomads_elegy,
                  nomads_requiem,
                  observatory_quest,
                  olafs_quest,
                  one_of_a_kind,
                  one_small_favour,
                  our_man_in_the_north,
                  the_path_of_glouphrie,
                  phite_club,
                  pieces_of_hate,
                  plague_city,
                  plagues_end,
                  the_prisoner_of_glouphrie,
                  quiet_before_the_swarm,
                  rag_and_bone_man,
                  ratcatchers,
                  recipe_for_disaster,
                  recruitment_drive,
                  regicide,
                  ritual_of_the_mahjarrat,
                  river_of_blood,
                  rocking_out,
                  roving_elves,
                  royal_trouble,
                  rum_deal,
                  rune_mechanics,
                  rune_memories,
                  salt_in_the_wound,
                  scorpion_catcher,
                  sea_slug,
                  shades_of_mortton,
                  shadow_of_the_storm,
                  sheep_herder,
                  shilo_village,
                  sliskes_endgame,
                  the_slug_menace,
                  smoking_kills,
                  some_like_it_cold,
                  spirit_of_summer,
                  spirits_of_the_elid,
                  summers_end,
                  swan_song,
                  tai_bwo_wannai_trio,
                  a_tail_of_two_cats,
                  the_tale_of_the_muspah,
                  tears_of_guthix,
                  the_temple_at_senntisten,
                  temple_of_ikov,
                  throne_of_miscellania,
                  toktz_ket_dill,
                  the_tourist_trap,
                  tower_of_life,
                  tree_gnome_village,
                  tribal_totem,
                  troll_romance,
                  troll_stronghold,
                  underground_pass,
                  a_void_dance,
                  the_void_stares_back,
                  wanted,
                  watchtower,
                  waterfall_quest,
                  what_lies_below,
                  while_guthix_sleeps,
                  within_the_light,
                  the_world_wakes,
                  "done"]

    for quest in all_quests:
        print(quest)


create_all_quests()
