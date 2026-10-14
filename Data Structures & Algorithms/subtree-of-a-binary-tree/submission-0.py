# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Agar subRoot khali (None) hai, toh khali tree hamesha subtree hota hai
        if not subRoot:
            return True

        # Agar main root khatam ho gaya par subRoot bacha hai, toh match nahi ho sakta
        if not root:
            return False

        # Agar is node se shuru hone wala tree subRoot ke bilkul barabar hai
        if self.isSameTree(root, subRoot):
            return True

        # Warna left ya right child me jaakar check karo
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # Agar dono nodes khali (None) hain, toh dono same hain
        if not s and not t:
            return True

        # Agar dono nodes exist karte hain aur dono ki value barabar hai
        if s and t and s.val == t.val:
            # Left aur right dono subtrees bhi match hone chahiye
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

        # Agar ek exist karta hai aur doosra nahi, ya value match nahi karti
        return False