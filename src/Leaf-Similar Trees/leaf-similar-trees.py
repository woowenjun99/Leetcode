from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []

        def dfs(src, sequence):
            if not src: return
            dfs(src.left, sequence)
            dfs(src.right, sequence)
            if not src.left and not src.right:
                sequence.append(src.val)

        dfs(root1, tree1)
        dfs(root2, tree2)
        return tree1 == tree2