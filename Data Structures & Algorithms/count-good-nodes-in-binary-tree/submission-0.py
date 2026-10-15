# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            # Agar current node ki value ab tak ke max se badi ya barabar hai, to ye good node hai
            res = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            
            # Left aur right subtrees se count add karein
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            
            return res
        
        return dfs(root, root.val)