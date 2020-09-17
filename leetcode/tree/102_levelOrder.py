import unittest
from collections import deque
from typing import List

from utils import stringToTreeNode, TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        d = deque()
        d.append(root)

        res = []
        while d:
            tmp = []
            for _ in range(len(d)):
                node = d.popleft()
                tmp.append(node.val)
                if node.left is not None:
                    d.append(node.left)
                if node.right is not None:
                    d.append(node.right)
            if len(tmp) > 0:
                res.append(tmp)
        return res


class Test(unittest.TestCase):
    def test_one(self):
        tree = '[3,9,20,null,null,15,7]'
        tree = stringToTreeNode(tree)
        answer = [
            [3],
            [9, 20],
            [15, 7]
        ]

        result = Solution().levelOrder(tree)
        self.assertEqual(answer, result)
