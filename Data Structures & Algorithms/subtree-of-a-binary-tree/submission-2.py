# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            left_same = isSame(p.left, q.left)
            right_same = isSame(p.right, q.right)

            return left_same and right_same

        if not subRoot:
            return True

        if not root:
            return False

        if isSame(root, subRoot):
            return True

        left_s = self.isSubtree(root.left, subRoot)
        right_s = self.isSubtree(root.right, subRoot)

        return left_s or right_s