import unittest
from cycle_checker import has_cycle


class TestGraphMethods(unittest.TestCase):

    def test_1_has_cycle(self):
        graph = {
            1: [2],
            2: [1, 5],
            3: [4],
            4: [3, 5],
            5: [2, 4, 10],
            6: [7, 10],
            7: [6, 8],
            8: [7, 9],
            9: [8],
            10: [5, 6]
        }
        self.assertEqual(has_cycle(graph), False)

    def test_2_has_cycle_(self):
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [2, 1]
        }
        self.assertEqual(has_cycle(graph), True)


    def test_3_has_cycle_(self):
        graph = {
            1: [2, 3, 4],
            2: [1, 5, 6],
            3: [1],
            4: [1, 8, 7],
            5: [2, 9, 10],
            6: [2, 10],
            7: [4, 11, 12],
            8: [4],
            9: [5],
            10: [5, 6],
            11: [7],
            12: [7]

        }
        self.assertEqual(has_cycle(graph), True)


if __name__ == '__main__':
    unittest.main()
