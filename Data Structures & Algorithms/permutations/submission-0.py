class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def f(idx):
            if idx == n:
                res.append(nums[:])
                return 

            for i in range(idx, n):
                nums[idx], nums[i] = nums[i], nums[idx]
                f(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        f(0)
        return res