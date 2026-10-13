# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            # 1. Traverse all the way to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left

            # 2. Visit the node with the current smallest value
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            # 3. Explore the right subtree
            curr = curr.right