# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        all_paths = []
        def dfs(node, path):
            if not node:
                return

            path.append(node.val)

            # If current node is a leaf, save a copy of this path
            if not node.left and not node.right:
                all_paths.append(path[:])
            else:
                dfs(node.left, path)

                dfs(node.right, path)
            path.pop()

        dfs(root, [])

        # Check every collected path
        for path in all_paths:
            # If any path sum equals targetSum, return True
            if sum(path) == targetSum:
                return True

        return False