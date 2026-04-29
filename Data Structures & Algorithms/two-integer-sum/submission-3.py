class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in h:
                return [h[x],i]
            h[nums[i]] = i
        return []
        # This is optimal solution with time complexity O(n)

        
        # Two pointer approach if the array is sorted then only we can use
        # Time Complexit: O(nlogn)
        # nums.sort()
        # l = 0 
        # r = len(nums) - 1
        # while l < r:
        #     if nums[l] + nums[r] == target:
        #         return [l, r]
        #     elif nums[l] + nums[r] < target:
        #         l += 1
        #     else:
        #         r -= 1


        # BruteForce method : O(n^2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):   
        #         if i < j and nums[i] + nums[j] == target:
        #             return [i, j]
    