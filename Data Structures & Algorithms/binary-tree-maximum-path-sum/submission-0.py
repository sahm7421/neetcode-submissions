# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # Compute max path downwards from children; discard negatives with max(..., 0)
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            # Max path sum with the current node as the apex/split
            res[0] = max(res[0], node.val + left_max + right_max)

            # Return max single branch back to parent
            return node.val + max(left_max, right_max)

        dfs(root)
        return res[0]