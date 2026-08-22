# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(root):
            if not root:
                return 0

            leftmax = dfs(root.left)
            rightmax = dfs(root.right)

            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)
            
            nonlocal res
            res = max(res, root.val + leftmax + rightmax)

            return max(leftmax, rightmax) + root.val

        dfs(root)
        return res
