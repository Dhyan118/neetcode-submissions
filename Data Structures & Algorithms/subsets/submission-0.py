class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def dhyan(idx, ds):
            res.append(ds[:])

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue

                ds.append(nums[i])
                dhyan(i + 1, ds)
                ds.pop()

        dhyan(0, [])
        return res