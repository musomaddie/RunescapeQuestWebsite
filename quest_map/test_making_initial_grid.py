import sys
import os
import unittest

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quest_map")])

from quest_map.grid_management import calculate_arrow
from quest_map.GridQuest import GridQuest
from quest_map.GridCell import GridCell


def draw_populated_scenario(dimensions, og, par):
    cells = [[GridCell((x, y)) for x in range(dimensions[0])]
             for y in range(dimensions[1])]
    og_quest = GridQuest("OG", (og[0], og[1]))
    cells[og[1]][og[0]].add_quest(og_quest)
    par_quest = GridQuest("PAR", (par[0], par[1]))
    cells[par[1]][par[0]].add_quest(par_quest)
    return (cells, og_quest, par_quest)


class ImmediatelyBelowTests(unittest.TestCase):
    def setUp(self):
        self.exit_results = [False, False, False, True, False]
        self.entry_results = [False, True, False, False, False]

    def test_even(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (2, 1), (0, 0), (1, 0))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_results,
                         cell_mapping[0][0].exit_points)
        self.assertEqual(self.entry_results,
                         cell_mapping[0][1].entry_points)

    def test_odd(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (3, 2), (1, 0), (2, 1))
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
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (2, 2), (0, 1), (1, 0))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_results,
                         cell_mapping[1][0].exit_points)
        self.assertEqual(self.entry_results,
                         cell_mapping[0][1].entry_points)

    def test_odd(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (3, 1), (1, 0), (2, 0))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_results,
                         cell_mapping[0][1].exit_points)
        self.assertEqual(self.entry_results,
                         cell_mapping[0][2].entry_points)


class DiagonallyBelow(unittest.TestCase):
    def setUp(self):
        self.exit_points = [False, False, False, False, True]
        self.entry_points = [True, False, False, False, False]

    def test_even(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (2, 2), (0, 0), (1, 1))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_points,
                         cell_mapping[0][0].exit_points)
        self.assertEqual(self.entry_points,
                         cell_mapping[1][1].entry_points)

    def test_odd(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (3, 3), (1, 0), (2, 2))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_points,
                         cell_mapping[0][1].exit_points)
        self.assertEqual(self.entry_points,
                         cell_mapping[2][2].entry_points)


class DiagonallyAbove(unittest.TestCase):
    def setUp(self):
        self.exit_points = [True, False, False, False, False]
        self.entry_points = [False, False, False, False, True]

    def test_even(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (3, 3), (0, 2), (1, 0))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_points,
                         cell_mapping[2][0].exit_points)
        self.assertEqual(self.entry_points,
                         cell_mapping[0][1].entry_points)

    def test_odd(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (3, 2), (1, 1), (2, 0))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_points,
                         cell_mapping[1][1].exit_points)
        self.assertEqual(self.entry_points,
                         cell_mapping[0][2].entry_points)


class FarBelow(unittest.TestCase):
    def setUp(self):
        self.exit_points = [False, False, False, False, True]
        self.entry_points = [True, False, False, False, False]

    def test_even(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (2, 3), (0, 0), (1, 2))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_points,
                         cell_mapping[0][0].exit_points)
        self.assertEqual(self.entry_points,
                         cell_mapping[2][1].entry_points)

    def test_odd(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (3, 4), (1, 0), (2, 3))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_points,
                         cell_mapping[0][1].exit_points)
        self.assertEqual(self.entry_points,
                         cell_mapping[3][2].entry_points)


class FarAbove(unittest.TestCase):
    def setUp(self):
        self.exit_points = [True, False, False, False, False]
        self.entry_points = [False, False, False, False, True]

    def test_even(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (2, 4), (0, 3), (1, 0))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_points,
                         cell_mapping[3][0].exit_points)
        self.assertEqual(self.entry_points,
                         cell_mapping[0][1].entry_points)

    def test_odd(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (3, 3), (1, 2), (2, 0))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_points,
                         cell_mapping[2][1].exit_points)
        self.assertEqual(self.entry_points,
                         cell_mapping[0][2].entry_points)


class DirectlyAcross(unittest.TestCase):
    def setUp(self):
        self.exit_points = [False, False, True, False, False]
        self.entry_points = [False, False, True, False, False]

    def test_even(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (3, 1), (0, 0), (2, 0))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_points,
                         cell_mapping[0][0].exit_points)
        self.assertEqual(self.entry_points,
                         cell_mapping[0][2].entry_points)

    def test_odd(self):
        cell_mapping, og_quest, par_quest = draw_populated_scenario(
            (4, 1), (1, 0), (3, 0))
        calculate_arrow(og_quest, par_quest, cell_mapping)
        self.assertEqual(self.exit_points,
                         cell_mapping[0][1].exit_points)
        self.assertEqual(self.entry_points,
                         cell_mapping[0][3].entry_points)


if __name__ == "__main__":
    log_file = "quest_map/testing_initial_creation.txt"
    f = open(log_file, 'w')
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)
    f.close()
