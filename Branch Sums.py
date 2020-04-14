# Write a function that takes in a Binary Tree and returns a list of its branch sums (ordered from leftmost branch sum to rightmost branch sum)
# A branch sum is the sum of all values in a Binary Tree branch.
# A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node


import unittest


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# O(N) time | O(N) space
# N = number of nodes


def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums


def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)


# --- Driver Program --- #


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1)
        self.assertEqual(branchSums(tree), [1])

    def test_case_2(self):
        tree = BinaryTree(1).insert([2])
        self.assertEqual(branchSums(tree), [3])

    def test_case_3(self):
        tree = BinaryTree(1).insert([2, 3])
        self.assertEqual(branchSums(tree), [3, 4])

    def test_case_4(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5])
        self.assertEqual(branchSums(tree), [7, 8, 4])

    def test_case_5(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])

    def test_case_6(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1])
        self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])

    def test_case_7(self):
        tree = BinaryTree(0)
        tree.left = BinaryTree(1)
        tree.left.left = BinaryTree(10)
        tree.left.left.left = BinaryTree(100)
        self.assertEqual(branchSums(tree), [111])

    def test_case_8(self):
        tree = BinaryTree(0)
        tree.left = BinaryTree(9)
        tree.right = BinaryTree(1)
        tree.right.right = BinaryTree(10)
        tree.right.right.right = BinaryTree(100)
        self.assertEqual(branchSums(tree), [111])

    def test_case_9(self):
        tree = BinaryTree(0)
        tree.left = BinaryTree(9)
        tree.right = BinaryTree(1)
        tree.right.left = BinaryTree(15)
        tree.right.right = BinaryTree(10)
        tree.right.right.left = BinaryTree(100)
        tree.right.right.right = BinaryTree(200)
        self.assertEqual(branchSums(tree), [9, 16, 111, 211])


class BinaryTree(BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return

        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)

            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i+1)

        return self
