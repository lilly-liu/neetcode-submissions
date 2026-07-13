# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(root):
            if not root:
                return 0
            lh = get_height(root.left)
            rh = get_height(root.right)
            return 1 + max(lh, rh)
        if not root:
            return True
        rh = get_height(root.right)
        lh = get_height(root.left)
        return abs(lh - rh) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)