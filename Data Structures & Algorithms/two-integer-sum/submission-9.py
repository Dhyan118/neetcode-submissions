class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in h: # check if its in hashmap 
                return [h[diff], i]
            h[n] = i # not in hashmap then we store it
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]