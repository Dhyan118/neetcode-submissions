# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            if left == -1 or right == -1 or abs(left - right) > 1: # this will check wether it is valid or not on left and right
                return -1

            return 1 + max(left, right) # This will get the height 

        return dfs(root) != -1 # If any other value is there 3 != -1 then true but -1 != -1 the false