class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, target, path):

            if target == 0:
                res.append(path[:])
                return

            if i == n or target < 0:
                return

            if nums[i] <= target:
                path.append(nums[i])
                dfs(i, target - nums[i], path)
                path.pop()

            dfs(i + 1, target, path)

        dfs(0, target, [])
        return res
