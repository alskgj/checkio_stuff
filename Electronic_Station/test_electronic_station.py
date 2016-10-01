import unittest

from .three_point_circle import checkio as tpc
from .numbers_factory import checkio as nf
from .brackets import checkio as brackets

from .color_map import is_solved as color_map_is_solved
from .color_map import is_valid as color_map_is_valid

class BasicTests(unittest.TestCase):
    def test_three_points_circle(self):
        self.assertEqual(tpc("(2,2),(6,2),(2,6)"), "(x-4)^2+(y-4)^2=2.83^2")
        self.assertEqual(tpc("(3,7),(6,9),(9,7)"), "(x-6)^2+(y-5.75)^2=3.25^2")

    def test_number_factory(self):
        self.assertEqual(nf(20), 45)
        self.assertEqual(nf(21),  37)
        self.assertEqual(nf(17), 0)
        self.assertEqual(nf(33),  0)


    def test_brackets(self):
        self.assertTrue(brackets("((5+3)*2+1)"))
        self.assertTrue(brackets("{[(3+1)+2]+}"))
        self.assertTrue(brackets("[1+1]+(2*2)-{3/3}"))
        self.assertTrue(brackets("2+3"))

        self.assertFalse(brackets("(3+{1-1)}"))
        self.assertFalse(brackets("(({[(((1)-2)+3)-3]/3}-3)"))

    def test_color_map_is_solved(self):
        self.assertTrue(color_map_is_solved({
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        },
            [1, 2, 3]))

        self.assertFalse(color_map_is_solved({
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        },
            [1, 2, 2]))

        self.assertFalse(color_map_is_solved({
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        },
            [1, 2, None]))

    def test_color_map_is_valid(self):
        self.assertFalse(color_map_is_valid({
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        },
            [1, 2, 2]))
        self.assertTrue(color_map_is_valid({
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        },
            [1, 2, None]))




if __name__ == "__main__":
    unittest.main()