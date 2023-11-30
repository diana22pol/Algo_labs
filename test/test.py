import unittest

from src.main import topological_sort

class TestTopologicalSort(unittest.TestCase):
    def test_topological_sort_1(self):
        dependecies = [('task2', 'task1'),
                       ('task3', 'task2'),
                       ('task4', 'task2'),
                       ('task5', 'task3'),
                       ('task5', 'task4')
                       ]
        expected = [
            'task1',
            'task2',
            'task3',
            'task4',
            'task5',
        ]

        self.assertEqual(topological_sort(dependecies), expected)