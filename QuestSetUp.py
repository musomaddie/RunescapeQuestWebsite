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
from quests.You_Are_It import You_Are_It
from quests.Zogre_Flesh_Eaters import Zogre_Flesh_Eaters

from questseries.Ariane_Signature_Heroes_Quests import Ariane_Signature_Heroes_Quests
from questseries.Desert_Series import Desert_Series
from questseries.Dragonkin_Series import Dragonkin_Series
from questseries.Druids_Circle_Series import Druids_Circle_Series
from questseries.Elder_Gods import Elder_Gods
from questseries.Elemental_Workshop_Series import Elemental_Workshop_Series
from questseries.Enchanted_Key_Series import Enchanted_Key_Series
from questseries.God_Series import God_Series
from questseries.Gnome_Series import Gnome_Series
from questseries.Linza_Signature_Heroes_Quests import Linza_Signature_Heroes_Quests
from questseries.Monkey_Series import Monkey_Series
from questseries.Penguin_Series import Penguin_Series
from questseries.Ozan_Signature_Heroes_Quests import Ozan_Signature_Heroes_Quests
from questseries.Sea_Slug_Series import Sea_Slug_Series
from questseries.Sir_Owen_Signature_Heroes_Quests import Sir_Owen_Signature_Heroes_Quests
from questseries.Temple_Knight_Series import Temple_Knight_Series
from questseries.The_Raptor_Signature_Heroes_Quests import The_Raptor_Signature_Heroes_Quests
from questseries.Xenia_Signature_Heroes_Quests import Xenia_Signature_Heroes_Quests


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

    you_are_it = You_Are_It()

    zogre_flesh_eaters = Zogre_Flesh_Eaters()

    # Setting up subquests
    missing_presumed_death.add_pre_quest(the_world_wakes)
    missing_presumed_death.add_pre_quest(ritual_of_the_mahjarrat)
    missing_presumed_death.add_pre_quest(the_death_of_chivalry)
    missing_presumed_death.add_pre_quest(the_chosen_commander)

    all_fired_up.add_pre_quest(priest_in_peril)
    animal_magnetism.add_pre_quest(ernest_the_chicken)
    animal_magnetism.add_pre_quest(priest_in_peril)
    animal_magnetism.add_pre_quest(the_restless_ghost)
    another_slice_of_ham.add_pre_quest(death_to_the_dorgeshuun)
    another_slice_of_ham.add_pre_quest(the_dig_site)
    another_slice_of_ham.add_pre_quest(the_giant_dwarf)
    as_a_first_resort.add_pre_quest(zogre_flesh_eaters)

    back_to_my_roots.add_pre_quest(fairy_tale_i_growing_pains)
    back_to_my_roots.add_pre_quest(the_hand_in_the_sand)
    back_to_my_roots.add_pre_quest(one_small_favour)
    back_to_my_roots.add_pre_quest(tribal_totem)
    back_to_the_freezer.add_pre_quest(ernest_the_chicken)
    back_to_the_freezer.add_pre_quest(some_like_it_cold)
    between_a_rock.add_pre_quest(dwarf_cannon)
    between_a_rock.add_pre_quest(fishing_contest)
    biohazard.add_pre_quest(plague_city)
    birthright_of_the_dwarves.add_pre_quest(king_of_the_dwarves)
    blood_runs_deep.add_pre_quest(dream_mentor)
    blood_runs_deep.add_pre_quest(glorious_memories)
    blood_runs_deep.add_pre_quest(horror_from_the_deep)
    the_branches_of_darkmeyer.add_pre_quest(legacy_of_seergaze)
    the_branches_of_darkmeyer.add_pre_quest(legends_quest)
    the_brink_of_extinction.add_pre_quest(the_elder_kiln)

    cabin_fever.add_pre_quest(pirates_treasure)
    cabin_fever.add_pre_quest(rum_deal)
    carnillean_rising.add_pre_quest(the_blood_pact)
    carnillean_rising.add_pre_quest(hazeel_cult)
    catapult_construction.add_pre_quest(regicide)
    children_of_mah.add_pre_quest(dishonour_among_thieves)
    children_of_mah.add_pre_quest(the_light_within)
    the_chosen_commander.add_pre_quest(land_of_the_goblins)
    a_clockwork_syringe.add_pre_quest(rocking_out)
    contact.add_pre_quest(icthlarins_little_helper)
    creature_of_fenkenstrain.add_pre_quest(priest_in_peril)
    creature_of_fenkenstrain.add_pre_quest(the_restless_ghost)
    crocodile_tears.add_pre_quest(dealing_with_scabaras)
    crocodile_tears.add_pre_quest(the_jack_of_spades)
    crocodile_tears.add_pre_quest(missing_my_mummy)
    crocodile_tears.add_pre_quest(spirits_of_the_elid)
    the_curse_of_arrav.add_pre_quest(defender_of_varrock)
    the_curse_of_arrav.add_pre_quest(missing_my_mummy)
    the_curse_of_arrav.add_pre_quest(shades_of_mortton)
    the_curse_of_arrav.add_pre_quest(the_tale_of_the_muspah)
    the_curse_of_arrav.add_pre_quest(troll_romance)

    darkness_of_hallowvale.add_pre_quest(in_aid_of_the_myreque)
    deadliest_catch.add_pre_quest(tower_of_life)
    dealing_with_scabaras.add_pre_quest(contact)
    dealing_with_scabaras.add_pre_quest(the_feud)
    dealing_with_scabaras.add_pre_quest(zogre_flesh_eaters)
    death_to_the_dorgeshuun.add_pre_quest(the_lost_tribe)
    desert_treasure.add_pre_quest(the_dig_site)
    desert_treasure.add_pre_quest(priest_in_peril)
    desert_treasure.add_pre_quest(temple_of_ikov)
    desert_treasure.add_pre_quest(the_tourist_trap)
    desert_treasure.add_pre_quest(troll_stronghold)
    desert_treasure.add_pre_quest(waterfall_quest)
    devious_minds.add_pre_quest(troll_stronghold)
    devious_minds.add_pre_quest(wanted)
    devious_minds.add_pre_quest(whats_mine_is_yours)
    diamond_in_the_rough.add_pre_quest(stolen_hearts)
    dimension_of_disaster.add_pre_quest(the_curse_of_arrav)
    dimension_of_disaster.add_pre_quest(shadow_of_the_storm)
    dishonour_among_thieves.add_pre_quest(hazeel_cult)
    dimension_of_disaster.add_pre_quest(missing_presumed_death)
    do_no_evil.add_pre_quest(recipe_for_disaster)
    dream_mentor.add_pre_quest(eadgars_ruse)
    dream_mentor.add_pre_quest(lunar_diplomacy)

    eadgars_ruse.add_pre_quest(druidic_ritual)
    eadgars_ruse.add_pre_quest(troll_stronghold)
    elemental_workshop_ii.add_pre_quest(elemental_workshop_i)
    elemental_workshop_iii.add_pre_quest(elemental_workshop_ii)
    elemental_workshop_iv.add_pre_quest(elemental_workshop_iv)
    evil_daves_big_day_out.add_pre_quest(recipe_for_disaster)
    the_eyes_of_glouphrie.add_pre_quest(the_grand_tree)

    fairy_tale_i_growing_pains.add_pre_quest(jungle_potion)
    fairy_tale_i_growing_pains.add_pre_quest(lost_city)
    fairy_tale_i_growing_pains.add_pre_quest(nature_spirit)
    fairy_tale_ii_cure_a_queen.add_pre_quest(fairy_tale_i_growing_pains)
    fairy_tale_iii_battle_at_orks_rift.add_pre_quest(
        fairy_tale_ii_cure_a_queen)
    fate_of_the_gods.add_pre_quest(missing_presumed_death)
    forgettable_tale.add_pre_quest(the_giant_dwarf)
    forgettable_tale.add_pre_quest(fishing_contest)
    forgiveness_of_a_chaos_dwarf.add_pre_quest(forgettable_tale)
    forgiveness_of_a_chaos_dwarf.add_pre_quest(between_a_rock)
    the_fremennik_isles.add_pre_quest(the_fremennik_trials)
    fur_n_seek.add_pre_quest(rag_and_bone_man)

    garden_of_tranquillity.add_pre_quest(creature_of_fenkenstrain)
    ghosts_ahoy.add_pre_quest(priest_in_peril)
    ghosts_ahoy.add_pre_quest(the_restless_ghost)
    glorious_memories.add_pre_quest(royal_trouble)
    glorious_memories.add_pre_quest(the_fremennik_isles)
    glorious_memories.add_pre_quest(mountain_daughter)
    the_great_brain_robbery.add_pre_quest(creature_of_fenkenstrain)
    the_great_brain_robbery.add_pre_quest(cabin_fever)
    the_great_brain_robbery.add_pre_quest(recipe_for_disaster)
    grim_tales.add_pre_quest(witchs_house)

    haunted_mine.add_pre_quest(priest_in_peril)
    haunted_mine.add_pre_quest(nature_spirit)
    heart_of_stone.add_pre_quest(carnillean_rising)
    heart_of_stone.add_pre_quest(rune_memories)
    heart_of_stone.add_pre_quest(rune_mechanics)
    heart_of_stone.add_pre_quest(the_elder_kiln)
    heros_welcome.add_pre_quest(lunar_diplomacy)
    heros_welcome.add_pre_quest(tai_bwo_wannai_trio)
    heroes_quest.add_pre_quest(shield_of_arrav)
    heroes_quest.add_pre_quest(lost_city)
    heroes_quest.add_pre_quest(dragon_slayer)
    heroes_quest.add_pre_quest(merlins_crystal)
    heroes_quest.add_pre_quest(druidic_ritual)
    holy_grail.add_pre_quest(merlins_crystal)
    hunt_for_red_raktuber.add_pre_quest(cold_war)
    hunt_for_red_raktuber.add_pre_quest(sea_slug)

    icthlarins_little_helper.add_pre_quest(diamond_in_the_rough)
    icthlarins_little_helper.add_pre_quest(gertrudes_cat)
    icthlarins_little_helper.add_pre_quest(the_restless_ghost)
    in_aid_of_the_myreque.add_pre_quest(in_search_of_the_myreque)
    in_search_of_the_myreque.add_pre_quest(nature_spirit)

    the_jack_of_spades.add_pre_quest(diamond_in_the_rough)

    kenniths_concerns.add_pre_quest(the_slug_menace)
    kindred_spirits.add_pre_quest(missing_presumed_death)
    king_of_the_dwarves.add_pre_quest(forgiveness_of_a_chaos_dwarf)
    king_of_the_dwarves.add_pre_quest(my_arms_big_adventure)
    kings_ransom.add_pre_quest(holy_grail)
    kings_ransom.add_pre_quest(murder_mystery)
    kings_ransom.add_pre_quest(one_small_favour)

    land_of_the_goblins.add_pre_quest(another_slice_of_ham)
    land_of_the_goblins.add_pre_quest(fishing_contest)
    legacy_of_seergaze.add_pre_quest(darkness_of_hallowvale)
    legends_quest.add_pre_quest(family_crest)
    legends_quest.add_pre_quest(heroes_quest)
    legends_quest.add_pre_quest(shilo_village)
    legends_quest.add_pre_quest(underground_pass)
    legends_quest.add_pre_quest(waterfall_quest)
    the_light_within.add_pre_quest(fate_of_the_gods)
    the_light_within.add_pre_quest(meeting_history)
    the_light_within.add_pre_quest(plagues_end)
    the_light_within.add_pre_quest(the_temple_at_senntisten)
    the_light_within.add_pre_quest(the_world_wakes)
    the_lord_of_vampyrium.add_pre_quest(the_branches_of_darkmeyer)
    the_lost_tribe.add_pre_quest(goblin_diplomacy)
    love_story.add_pre_quest(swan_song)
    love_story.add_pre_quest(recipe_for_disaster)
    lunar_diplomacy.add_pre_quest(lost_city)
    lunar_diplomacy.add_pre_quest(the_fremennik_trials)
    lunar_diplomacy.add_pre_quest(shilo_village)

    making_history.add_pre_quest(the_restless_ghost)
    making_history.add_pre_quest(priest_in_peril)
    meeting_history.add_pre_quest(meeting_history)
    the_mighty_fall.add_pre_quest(missing_presumed_death)
    the_mighty_fall.add_pre_quest(the_chosen_commander)
    the_mighty_fall.add_pre_quest(my_arms_big_adventure)
    the_mighty_fall.add_pre_quest(what_lies_below)
    missing_my_mummy.add_pre_quest(the_golem)
    missing_my_mummy.add_pre_quest(icthlarins_little_helper)
    monkey_madness.add_pre_quest(the_grand_tree)
    monkey_madness.add_pre_quest(tree_gnome_village)
    mournings_end_part_i.add_pre_quest(big_chompy_bird_hunting)
    mournings_end_part_i.add_pre_quest(sheep_herder)
    mournings_end_part_i.add_pre_quest(roving_elves)
    mournings_end_part_ii.add_pre_quest(mournings_end_part_i)
    my_arms_big_adventure.add_pre_quest(eadgars_ruse)
    my_arms_big_adventure.add_pre_quest(the_feud)
    my_arms_big_adventure.add_pre_quest(jungle_potion)

    nature_spirit.add_pre_quest(priest_in_peril)
    nature_spirit.add_pre_quest(the_restless_ghost)
    nomads_elegy.add_pre_quest(dishonour_among_thieves)
    nomads_elegy.add_pre_quest(heart_of_stone)
    nomads_elegy.add_pre_quest(the_mighty_fall)
    nomads_elegy.add_pre_quest(throne_of_miscellania)
    nomads_elegy.add_pre_quest(nomads_requiem)
    nomads_elegy.add_pre_quest(the_void_stares_back)
    nomads_elegy.add_pre_quest(while_guthix_sleeps)
    nomads_elegy.add_pre_quest(blood_runs_deep)
    nomads_requiem.add_pre_quest(kings_ransom)

    olafs_quest.add_pre_quest(the_fremennik_trials)
    one_of_a_kind.add_pre_quest(a_tail_of_two_cats)
    one_of_a_kind.add_pre_quest(the_world_wakes)
    one_of_a_kind.add_pre_quest(kings_ransom)
    one_of_a_kind.add_pre_quest(missing_presumed_death)
    one_small_favour.add_pre_quest(rune_mysteries)
    one_small_favour.add_pre_quest(shilo_village)
    our_man_in_the_north.add_pre_quest(do_no_evil)
    our_man_in_the_north.add_pre_quest(crocodile_tears)

    the_path_of_glouphrie.add_pre_quest(waterfall_quest)
    the_path_of_glouphrie.add_pre_quest(the_eyes_of_glouphrie)
    the_path_of_glouphrie.add_pre_quest(tree_gnome_village)
    phite_club.add_pre_quest(our_man_in_the_north)
    pieces_of_hate.add_pre_quest(gertrudes_cat)
    pieces_of_hate.add_pre_quest(a_clockwork_syringe)
    plagues_end.add_pre_quest(making_history)
    plagues_end.add_pre_quest(within_the_light)
    pieces_of_hate.add_pre_quest(catapult_construction)
    pieces_of_hate.add_pre_quest(within_the_light)
    the_prisoner_of_glouphrie.add_pre_quest(the_path_of_glouphrie)
    the_prisoner_of_glouphrie.add_pre_quest(roving_elves)
    quiet_before_the_swarm.add_pre_quest(imp_catcher)
    quiet_before_the_swarm.add_pre_quest(wanted)

    ratcatchers.add_pre_quest(icthlarins_little_helper)
    recipe_for_disaster.add_pre_quest(cooks_assistant)
    recipe_for_disaster.add_pre_quest(goblin_diplomacy)
    recipe_for_disaster.add_pre_quest(fishing_contest)
    recipe_for_disaster.add_pre_quest(gertrudes_cat)
    recipe_for_disaster.add_pre_quest(shadow_of_the_storm)
    recipe_for_disaster.add_pre_quest(big_chompy_bird_hunting)
    recipe_for_disaster.add_pre_quest(biohazard)
    recipe_for_disaster.add_pre_quest(demon_slayer)
    recipe_for_disaster.add_pre_quest(murder_mystery)
    recipe_for_disaster.add_pre_quest(nature_spirit)
    recipe_for_disaster.add_pre_quest(witchs_house)
    recipe_for_disaster.add_pre_quest(lost_city)
    recipe_for_disaster.add_pre_quest(legends_quest)
    recipe_for_disaster.add_pre_quest(monkey_madness)
    recipe_for_disaster.add_pre_quest(desert_treasure)
    recipe_for_disaster.add_pre_quest(horror_from_the_deep)
    regicide.add_pre_quest(underground_pass)
    ritual_of_the_mahjarrat.add_pre_quest(enakhras_lament)
    ritual_of_the_mahjarrat.add_pre_quest(fight_arena)
    ritual_of_the_mahjarrat.add_pre_quest(hazeel_cult)
    ritual_of_the_mahjarrat.add_pre_quest(rocking_out)
    ritual_of_the_mahjarrat.add_pre_quest(the_slug_menace)
    ritual_of_the_mahjarrat.add_pre_quest(a_tail_of_two_cats)
    ritual_of_the_mahjarrat.add_pre_quest(the_temple_at_senntisten)
    ritual_of_the_mahjarrat.add_pre_quest(while_guthix_sleeps)
    river_of_blood.add_pre_quest(the_lord_of_vampyrium)
    rocking_out.add_pre_quest(the_great_brain_robbery)
    roving_elves.add_pre_quest(waterfall_quest)
    roving_elves.add_pre_quest(regicide)
    royal_trouble.add_pre_quest(throne_of_miscellania)
    rum_deal.add_pre_quest(priest_in_peril)
    rum_deal.add_pre_quest(zogre_flesh_eaters)
    rune_memories.add_pre_quest(rune_mysteries)

    salt_in_the_wound.add_pre_quest(kenniths_concerns)
    shadow_of_the_storm.add_pre_quest(demon_slayer)
    shadow_of_the_storm.add_pre_quest(the_golem)
    shilo_village.add_pre_quest(jungle_potion)
    sliskes_endgame.add_pre_quest(the_death_of_chivalry)
    sliskes_endgame.add_pre_quest(children_of_mah)
    sliskes_endgame.add_pre_quest(heros_welcome)
    sliskes_endgame.add_pre_quest(kindred_spirits)
    sliskes_endgame.add_pre_quest(nomads_elegy)
    sliskes_endgame.add_pre_quest(one_of_a_kind)
    the_slug_menace.add_pre_quest(sea_slug)
    the_slug_menace.add_pre_quest(wanted)
    smoking_kills.add_pre_quest(icthlarins_little_helper)
    some_like_it_cold.add_pre_quest(hunt_for_red_raktuber)
    spirit_of_summer.add_pre_quest(the_restless_ghost)
    summers_end.add_pre_quest(spirit_of_summer)
    swan_song.add_pre_quest(garden_of_tranquillity)
    swan_song.add_pre_quest(one_small_favour)

    tai_bwo_wannai_trio.add_pre_quest(jungle_potion)
    a_tail_of_two_cats.add_pre_quest(icthlarins_little_helper)
    the_temple_at_senntisten.add_pre_quest(desert_treasure)
    the_temple_at_senntisten.add_pre_quest(devious_minds)
    the_temple_at_senntisten.add_pre_quest(the_curse_of_arrav)
    throne_of_miscellania.add_pre_quest(heroes_quest)
    throne_of_miscellania.add_pre_quest(the_fremennik_trials)
    troll_romance.add_pre_quest(troll_stronghold)
    troll_stronghold.add_pre_quest(death_plateau)

    underground_pass.add_pre_quest(biohazard)

    a_void_dance.add_pre_quest(quiet_before_the_swarm)
    a_void_dance.add_pre_quest(druidic_ritual)
    the_void_stares_back.add_pre_quest(a_void_dance)

    wanted.add_pre_quest(recruitment_drive)
    wanted.add_pre_quest(the_lost_tribe)
    wanted.add_pre_quest(priest_in_peril)
    while_guthix_sleeps.add_pre_quest(defender_of_varrock)
    while_guthix_sleeps.add_pre_quest(dream_mentor)
    while_guthix_sleeps.add_pre_quest(the_hand_in_the_sand)
    while_guthix_sleeps.add_pre_quest(kings_ransom)
    while_guthix_sleeps.add_pre_quest(legends_quest)
    while_guthix_sleeps.add_pre_quest(mournings_end_part_ii)
    while_guthix_sleeps.add_pre_quest(the_path_of_glouphrie)
    while_guthix_sleeps.add_pre_quest(recipe_for_disaster)
    while_guthix_sleeps.add_pre_quest(summers_end)
    while_guthix_sleeps.add_pre_quest(swan_song)
    while_guthix_sleeps.add_pre_quest(tears_of_guthix)
    while_guthix_sleeps.add_pre_quest(wanted)
    while_guthix_sleeps.add_pre_quest(wolf_whistle)
    while_guthix_sleeps.add_pre_quest(zogre_flesh_eaters)
    while_guthix_sleeps.add_pre_quest(what_lies_below)
    within_the_light.add_pre_quest(mournings_end_part_ii)
    the_world_wakes.add_pre_quest(ritual_of_the_mahjarrat)
    the_world_wakes.add_pre_quest(the_chosen_commander)
    the_world_wakes.add_pre_quest(the_void_stares_back)
    the_world_wakes.add_pre_quest(the_branches_of_darkmeyer)
    the_world_wakes.add_pre_quest(the_firemakers_curse)

    zogre_flesh_eaters.add_pre_quest(big_chompy_bird_hunting)
    zogre_flesh_eaters.add_pre_quest(jungle_potion)

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
                  you_are_it,
                  zogre_flesh_eaters]

    ariane = Ariane_Signature_Heroes_Quests()
    ariane.add_quest(rune_mysteries)
    ariane.add_quest(rune_memories)
    ariane.add_quest(heart_of_stone)

    desert_series = Desert_Series()
    desert_series.add_quest(stolen_hearts)
    desert_series.add_quest(diamond_in_the_rough)
    desert_series.add_quest(icthlarins_little_helper)
    desert_series.add_quest(spirits_of_the_elid)
    desert_series.add_quest(contact)
    desert_series.add_quest(dealing_with_scabaras)
    desert_series.add_quest(smoking_kills)
    desert_series.add_quest(missing_my_mummy)
    desert_series.add_quest(the_jack_of_spades)
    desert_series.add_quest(crocodile_tears)
    desert_series.add_quest(do_no_evil)
    desert_series.add_quest(our_man_in_the_north)
    desert_series.add_quest(phite_club)

    dragonkin_series = Dragonkin_Series()
    dragonkin_series.add_quest(a_tail_of_two_cats)
    dragonkin_series.add_quest(while_guthix_sleeps)
    dragonkin_series.add_quest(ritual_of_the_mahjarrat)
    dragonkin_series.add_quest(missing_presumed_death)
    dragonkin_series.add_quest(one_of_a_kind)
    dragonkin_series.add_quest(heros_welcome)
    dragonkin_series.add_quest(sliskes_endgame)

    druids_circles_series = Druids_Circle_Series()
    druids_circles_series.add_quest(druidic_ritual)
    druids_circles_series.add_quest(eadgars_ruse)
    druids_circles_series.add_related_quest(while_guthix_sleeps)
    druids_circles_series.add_related_quest(the_world_wakes)

    elder_gods = Elder_Gods()
    elder_gods.add_quest(fate_of_the_gods)
    elder_gods.add_quest(heart_of_stone)
    elder_gods.add_quest(children_of_mah)
    elder_gods.add_quest(sliskes_endgame)
    elder_gods.add_related_quest(one_of_a_kind)

    elemental_workshop_series = Elemental_Workshop_Series()
    elemental_workshop_series.add_quest(elemental_workshop_i)
    elemental_workshop_series.add_quest(elemental_workshop_ii)
    elemental_workshop_series.add_quest(elemental_workshop_iii)
    elemental_workshop_series.add_quest(elemental_workshop_iv)

    enchanted_key_series = Enchanted_Key_Series()
    enchanted_key_series.add_quest(making_history)
    enchanted_key_series.add_quest(meeting_history)
    enchanted_key_series.add_quest(the_light_within)

    god_series = God_Series()
    god_series.add_quest(the_world_wakes)
    god_series.add_quest(the_death_of_chivalry)
    god_series.add_quest(missing_presumed_death)
    god_series.add_quest(fate_of_the_gods)
    god_series.add_quest(the_mighty_fall)
    god_series.add_quest(dishonour_among_thieves)
    god_series.add_quest(heros_welcome)
    god_series.add_quest(the_light_within)
    god_series.add_quest(nomads_elegy)
    god_series.add_quest(children_of_mah)
    god_series.add_quest(sliskes_endgame)

    gnome_series = Gnome_Series()
    gnome_series.add_quest(the_grand_tree)
    gnome_series.add_quest(monkey_madness)
    gnome_series.add_quest(the_eyes_of_glouphrie)
    gnome_series.add_quest(the_path_of_glouphrie)
    gnome_series.add_quest(the_prisoner_of_glouphrie)
    gnome_series.add_related_quest(tree_gnome_village)
    gnome_series.add_related_quest(waterfall_quest)
    gnome_series.add_related_quest(roving_elves)

    linza = Linza_Signature_Heroes_Quests()
    linza.add_quest(deadliest_catch)
    linza.add_quest(kindred_spirits)

    monkey_series = Monkey_Series()
    monkey_series.add_quest(monkey_madness)
    monkey_series.add_quest(recipe_for_disaster)
    monkey_series.add_quest(do_no_evil)

    penguin_series = Penguin_Series()
    penguin_series.add_quest(cold_war)
    penguin_series.add_quest(hunt_for_red_raktuber)
    penguin_series.add_quest(some_like_it_cold)
    penguin_series.add_quest(back_to_the_freezer)
    penguin_series.add_related_quest(recipe_for_disaster)

    ozan = Ozan_Signature_Heroes_Quests()
    ozan.add_quest(stolen_hearts)
    ozan.add_quest(diamond_in_the_rough)
    ozan.add_quest(the_jack_of_spades)

    sea_slug_series = Sea_Slug_Series()
    sea_slug_series.add_quest(sea_slug)
    sea_slug_series.add_quest(the_slug_menace)
    sea_slug_series.add_quest(kenniths_concerns)
    sea_slug_series.add_quest(salt_in_the_wound)
    sea_slug_series.add_related_quest(rum_deal)
    sea_slug_series.add_related_quest(hunt_for_red_raktuber)
    sea_slug_series.add_related_quest(evil_daves_big_day_out)

    sir_owen = Sir_Owen_Signature_Heroes_Quests()
    sir_owen.add_quest(the_death_of_chivalry)

    temple_knight_series = Temple_Knight_Series()
    temple_knight_series.add_quest(recruitment_drive)
    temple_knight_series.add_quest(wanted)
    temple_knight_series.add_quest(the_slug_menace)
    temple_knight_series.add_quest(while_guthix_sleeps)
    temple_knight_series.add_quest(ritual_of_the_mahjarrat)
    temple_knight_series.add_quest(the_death_of_chivalry)
    temple_knight_series.add_related_quest(devious_minds)

    the_raptor = The_Raptor_Signature_Heroes_Quests()
    the_raptor.add_quest(song_from_the_depths)

    xenia = Xenia_Signature_Heroes_Quests()
    xenia.add_quest(the_blood_pact)
    xenia.add_quest(carnillean_rising)
    xenia.add_quest(heart_of_stone)
    xenia.add_quest(nomads_elegy)

    all_quest_series = [ariane,
                        desert_series,
                        dragonkin_series,
                        druids_circles_series,
                        elder_gods,
                        elemental_workshop_series,
                        enchanted_key_series,
                        god_series,
                        gnome_series,
                        linza,
                        monkey_series,
                        penguin_series,
                        ozan,
                        sea_slug_series,
                        sir_owen,
                        the_raptor,
                        xenia,
                        "done"
                        ]

    print(all_quest_series)

    return all_quests


create_all_quests()
