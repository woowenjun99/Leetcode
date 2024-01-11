from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.max_difference = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Postorder traversal
        def postorder_traversal(node):
            if not node: return [None, None]
    
            left = postorder_traversal(node.left)
            right = postorder_traversal(node.right)
            four_values = [x for x in [left[0], left[1], right[0], right[1], node.val] if x != None]
            biggest = max(four_values)
            smallest = min(four_values)
            self.max_difference = max(self.max_difference, abs(node.val - biggest), abs(node.val - smallest))
            return [smallest, biggest]

        postorder_traversal(root)

        return self.max_difference