class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, target, curr):
            if target == 0:
                res.append(curr[:])
                return

            if i == len(nums) or target < 0:
                return

            if nums[i] <= target:
                curr.append(nums[i])
                dfs(i, target - nums[i], curr)
                curr.pop()

            dfs(i + 1, target, curr)

        dfs(0, target, [])
        return res