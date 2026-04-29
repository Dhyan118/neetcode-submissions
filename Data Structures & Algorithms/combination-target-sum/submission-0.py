class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def Dhyan(idx, target, path):
            if target == 0:
                res.append(path[:])
                return

            if idx == n or target < 0:
                return
                
            if nums[idx] <= target:
                path.append(nums[idx])
                Dhyan(idx, target-nums[idx], path)
                path.pop()

            Dhyan(idx + 1, target, path)

        Dhyan(0, target, [])
        return res
