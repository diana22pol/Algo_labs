import unittest
from tree import branchSums, BinaryTree


class TestBranchSums(unittest.TestCase):
    def test_with_1_root(self):
        root = BinaryTree(5)
        result = branchSums(root)
        self.assertEqual(result, 0)

    def test_with_1_root_and_left_leaf(self):
        root = BinaryTree(5)
        root.left = BinaryTree(3)
        root.right = None
        result = branchSums(root)
        self.assertEqual(result, 3)

    def test_with_1_root_and_left_left_leaf(self):
        root = BinaryTree(5)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(2)
        root.right = None
        result = branchSums(root)
        self.assertEqual(result, 2)

    def test_with_left_and_right_leafs(self):
        root = BinaryTree(5)
        root.left = BinaryTree(3)
        root.right = BinaryTree(9)
        result = branchSums(root)
        self.assertEqual(result, 3)

    def test_with_right_left_and_left_left_leafs(self):
        root = BinaryTree(5)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(1)
        root.right = BinaryTree(9)
        root.right.left = BinaryTree(7)
        result = branchSums(root)
        self.assertEqual(result, 8)

    def test_with_right_left_and_left_left_left_leafs(self):
        root = BinaryTree(5)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(2)
        root.right = BinaryTree(9)
        root.right.left = BinaryTree(7)
        result = branchSums(root)
        self.assertEqual(result, 9)

    def test_with_right_left_and_left_left_left_leafs(self):
        root = BinaryTree(100)
        root.left = BinaryTree(90)
        root.left.left = BinaryTree(80)
        root.right = BinaryTree(110)
        root.right.left = BinaryTree(105)
        root.right.right = BinaryTree(115)
        root.left.right = BinaryTree(95)
        root.right.right.left = BinaryTree(113)
        root.left.left.left = BinaryTree(50)

        result = branchSums(root)
        self.assertEqual(result, 268)


if __name__ == '__main__':
    unittest.main()