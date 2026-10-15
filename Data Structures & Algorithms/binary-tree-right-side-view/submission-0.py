from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        q = deque([root])
        
        while q:
            right_val = None
            for _ in range(len(q)):
                node = q.popleft()
                right_val = node.val  # Overwrite with the latest node in this level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(right_val)
            
        return res