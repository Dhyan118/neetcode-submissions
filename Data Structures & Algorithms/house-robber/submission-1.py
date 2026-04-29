class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        prev2, prev = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(nums[i] + prev2, prev)
            prev2, prev = prev, curr

        return prev
        