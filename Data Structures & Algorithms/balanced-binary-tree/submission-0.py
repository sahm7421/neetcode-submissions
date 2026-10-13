# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1:
                return -1

            right = dfs(node.right)
            if right == -1:
                return -1

            # If current node is unbalanced, propagate -1 upwards
            if abs(left - right) > 1:
                return -1

            # Return height of the current subtree
            return 1 + max(left, right)

        return dfs(root) != -1