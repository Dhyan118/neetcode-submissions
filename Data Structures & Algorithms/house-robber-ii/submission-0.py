class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(house):
            i, j = 0, 0
            for n in house:
                new_rob = max(j, i +n)
                i = j
                j = new_rob
            return j

        return max(helper(nums[:-1]), helper(nums[1:]))

        