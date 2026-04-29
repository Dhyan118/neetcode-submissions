class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dhyanmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in Dhyanmap:
                return [Dhyanmap[diff], i]
            Dhyanmap[n] = i
        return
        