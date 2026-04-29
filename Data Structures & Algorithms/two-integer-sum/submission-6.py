class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in h:
                return [h[diff], i]
            h[j] = i
        