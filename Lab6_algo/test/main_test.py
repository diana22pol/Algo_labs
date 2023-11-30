import unittest

from src.main import find_substring_indices


class TestFindSubstringIndices(unittest.TestCase):
    def test(self):
        self.assertEqual(find_substring_indices("sssenneeennnssssnsssseensennneeensss", "seen"), [20])

    def test_1(self):
        self.assertEqual(find_substring_indices("абракадабра", "абра"), [0, 7])

    def test_2(self):
        self.assertEqual(find_substring_indices("hello world", "world"), [6])

    def test_3(self):
        self.assertEqual(find_substring_indices("hello world", "goodbye"), [])

    def test_4(self):
        self.assertEqual(find_substring_indices("aaaaa", "aa"), [0, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()


