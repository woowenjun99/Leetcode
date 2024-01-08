from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        response = []
    
        def inorder(v):
            if not v: return
            inorder(v.left)
            if v.val >= low and v.val <= high: response.append(v.val)
            inorder(v.right)
        
        inorder(root)
        return sum(response)