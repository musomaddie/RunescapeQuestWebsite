import sys
import os
import unittest

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quest_map")])

from quest_map.grid_management import calculate_arrow
from quest_map.GridQuest import GridQuest
from quest_map.GridCell import GridCell


def draw_blank_scenario(width, height):
    return [[GridCell((x, y)) for x in range(width)] for y in range(height)]


def add_quest(width, height, cells, q_type="OG"):
    quest = GridQuest("OG", (width, height))
    if q_type == "PAR":
        quest.name = "PAR"
    cells[height][width].add_quest(quest)
    return quest


class ImmediatelyBelowTests(unittest.TestCase):
    def setUp(self):
        self.exit_results = [False, False, False, True, False]
        self.entry_results = [False, True, False, False, False]

    def test_even(self):
        cell_mapping = draw_blank_scenario(2, 1)
        og_quest = add_quest(0, 0, cell_mapping)
        par_quest = add_quest(1, 0, cell_mapping, "PAR")
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_results,
                         cell_mapping[0][0].exit_points)
        self.assertEqual(self.entry_results,
                         cell_mapping[0][1].entry_points)

    def test_odd(self):
        cell_mapping = draw_blank_scenario(3, 2)
        og_quest = add_quest(1, 0, cell_mapping)
        par_quest = add_quest(2, 1, cell_mapping, "PAR")
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_results,
                         cell_mapping[0][1].exit_points)
        self.assertEqual(self.entry_results,
                         cell_mapping[1][2].entry_points)


class ImmediatelyAboveTestCases(unittest.TestCase):

    def setUp(self):
        self.exit_results = [False, True, False, False, False]
        self.entry_results = [False, False, False, True, False]

    def test_even(self):
        cell_mapping = draw_blank_scenario(2, 2)
        og_quest = add_quest(0, 1, cell_mapping)
        par_quest = add_quest(1, 0, cell_mapping, "PAR")
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_results,
                         cell_mapping[1][0].exit_points)
        self.assertEqual(self.entry_results,
                         cell_mapping[0][1].entry_points)

    def test_odd(self):
        cell_mapping = draw_blank_scenario(3, 1)
        og_quest = add_quest(1, 0, cell_mapping)
        par_quest = add_quest(2, 0, cell_mapping, "PAR")
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_results,
                         cell_mapping[0][1].exit_points)
        self.assertEqual(self.entry_results,
                         cell_mapping[0][2].entry_points)


class DiagonallyBelow(unittest.TestCase):
    def test_even(self):
        cell_mapping = draw_blank_scenario(2, 2)
        og_quest = add_quest(0, 0, cell_mapping)
        par_quest = add_quest(1, 1, cell_mapping, "PAR")
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual([False, False, False, False, True],
                         cell_mapping[0][0].exit_points)
        self.assertEqual([True, False, False, False, False],
                         cell_mapping[1][1].entry_points)

    def test_odd(self):
        cell_mapping = draw_blank_scenario(3, 3)
        og_quest = add_quest(1, 0, cell_mapping)
        par_quest = add_quest(2, 2, cell_mapping, "PAR")
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual([False, False, False, False, True],
                         cell_mapping[0][1].exit_points)
        self.assertEqual([True, False, False, False, False],
                         cell_mapping[2][2].entry_points)


if __name__ == "__main__":
    log_file = "quest_map/testing_initial_creation.txt"
    f = open(log_file, 'w')
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)
    f.close()
