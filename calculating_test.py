import unittest

from calculating import Calculate


class TestFindThreeNumbers(unittest.TestCase):

    def test_find_three_numbers(self):
        self.assertEqual(Calculate([5, 1, 2, 8, 9, 3], 6), True)


if __name__ == '__main__':
     unittest.main()

