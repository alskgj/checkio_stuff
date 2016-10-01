import unittest

from .three_point_circle import checkio as tpc
from .numbers_factory import checkio as nf


class BasicTests(unittest.TestCase):
    def test_three_points_circle(self):
        self.assertEqual(tpc("(2,2),(6,2),(2,6)"), "(x-4)^2+(y-4)^2=2.83^2")
        self.assertEqual(tpc("(3,7),(6,9),(9,7)"), "(x-6)^2+(y-5.75)^2=3.25^2")

    def test_number_factory(self):
        self.assertEqual(nf(20), 45)
        self.assertEqual(nf(21),  37)
        self.assertEqual(nf(17), 0)
        self.assertEqual(nf(33),  0)


if __name__ == "__main__":
    unittest.main()