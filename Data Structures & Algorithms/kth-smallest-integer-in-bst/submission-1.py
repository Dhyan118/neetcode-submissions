# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None 

        def dfs(curr):
            nonlocal count, ans

            if not curr or ans is not None:
                return

            dfs(curr.left) # go left side

            count += 1
            if count == k:
                ans = curr.val
                return

            dfs(curr.right) 
        dfs(root)
        return ans