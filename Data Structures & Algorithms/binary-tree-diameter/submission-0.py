# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(curr: Optional[TreeNode]) -> int:
            nonlocal res
            if not curr:
                return 0

            # Find the height of left and right subtrees
            left = dfs(curr.left)
            right = dfs(curr.right)

            # Update the maximum diameter passing through the current node
            res = max(res, left + right)

            # Return height of the current subtree
            return 1 + max(left, right)

        dfs(root)
        return res