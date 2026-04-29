class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        j = 1
        for i in range(len(nums) - 1 ):
            if nums[i] == nums[j]:
                return True
            else:
                j += 1
        return False