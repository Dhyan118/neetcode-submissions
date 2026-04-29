class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def Dhyan(idx, ds):
            res.append(ds[:])

            for i in range(idx, n):
                if i > idx and nums[i] == nums[i - 1]:
                    continue 
                    

                ds.append(nums[i])
                Dhyan(i+ 1, ds)
                ds.pop()

        Dhyan(0, [])

        return res


        