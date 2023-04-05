# https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(root_):
            if not root_:
                return
            inorder(root_.left)
            result.append(root_.val)
            inorder(root_.right)

        inorder(root)
        return result
