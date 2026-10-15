# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low, high):
            if not node:
                return True
            
            # Current node value strictly (low, high) ke beech honi chahiye
            if not (low < node.val < high):
                return False
            
            # Left subtree: upper limit becomes node.val
            # Right subtree: lower limit becomes node.val
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)
        
        return valid(root, float("-inf"), float("inf"))