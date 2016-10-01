import unittest

from .bird_language import translate
from .rotate import rotate
from .probably_dice import probability


class BasicTests(unittest.TestCase):
    def test_bird(self):
        self.assertEqual(translate("hieeelalaooo"), "hello")
        self.assertEqual(translate("hoooowe yyyooouuu duoooiiine"), "how you doin")
        self.assertEqual(translate("aaa bo cy da eee fe"), "a b c d e f")
        self.assertEqual(translate("sooooso aaaaaaaaa"), "sos aaa")

    def test_rotate(self):
        self.assertEqual(rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]), [1, 8])
        self.assertEqual(rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]), [])
        self.assertEqual(rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]), [0])
        self.assertEqual(rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]), [0, 5])

    def test_probability(self):
        self.assertEqual(probability(2, 6, 3), 0.0556)  # 2 six-sided dice have a 5.56% chance of totalling 3
        self.assertEqual(probability(2, 6, 4), 0.0833)
        self.assertEqual(probability(2, 6, 7), 0.1667)
        self.assertEqual(probability(2, 3, 5), 0.2222)  # 2 three-sided dice have a 22.22% chance of totalling 5
        self.assertEqual(probability(2, 3, 7), 0)  # The maximum you can roll on 2 three-sided dice is 6
        self.assertEqual(probability(3, 6, 7), 0.0694)
        self.assertEqual(probability(10, 10, 50), 0.0375)


if __name__ == "__main__":
    unittest.main()