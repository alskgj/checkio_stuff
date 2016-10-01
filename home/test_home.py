import unittest

from .roman_numeral import checkio as roman
from .flat_dictionary import flatten
from .pawn_brotherhood import safe_pawns
from .min_and_max import min, max

class BasicTests(unittest.TestCase):

    def test_roman(self):
        self.assertEqual(roman(6), 'VI')
        self.assertEqual(roman(76), 'LXXVI')
        self.assertEqual(roman(13), 'XIII')
        self.assertEqual(roman(44), 'XLIV')
        self.assertEqual(roman(3999), 'MMMCMXCIX')

    def test_flat(self):
        self.assertEqual(flatten({"key": "value"}), {"key": "value"})
        self.assertEqual(flatten({"key": {"deeper": {"more": {"enough": "value"}}}}),
                         {"key/deeper/more/enough": "value"})
        self.assertEqual(flatten({"empty": {}}), {"empty": ""})

    def test_pawns(self):
        self.assertEqual(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}), 6)
        self.assertEqual(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}), 1)

    def test_min_max(self):
        self.assertEqual(max(3, 2), 3)
        self.assertEqual(min(3, 2), 2)
        self.assertEqual(max([1, 2, 0, 3, 4]), 4)
        self.assertEqual(min("hello"), "e")
        self.assertEqual(max(2.2, 5.6, 5.9, key=int), 5.6)
        self.assertEqual(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]), [9, 0])


if __name__ == "__main__":
    unittest.main()
