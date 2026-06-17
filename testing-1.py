import unittest
from score import calculate_score

class TestScore(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            calculate_score(8, 2),
            7.5
        )

    def test_no_wrong_answers(self):
        self.assertEqual(
            calculate_score(10, 0),
            10
        )

    def test_missing_values(self):
        self.assertEqual(
            calculate_score(),
            0
        )

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            calculate_score(-1, 2)

if __name__ == "__main__":
    unittest.main()