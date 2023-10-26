class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    return BranchSumscount(root, False)


def BranchSumscount (node, is_left):
    if node is None:
        return 0

    if node.left is None and node.right is None and is_left:
        return node.value

    left_sum = BranchSumscount(node.left, True)
    right_sum = BranchSumscount(node.right, False)

    return left_sum + right_sum

