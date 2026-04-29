class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        curr_end = 0
        farthest = 0
        # We don't need to jump from the last index
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            # If we've reached the end of the current jump range
            if i == curr_end:
                jump += 1
                curr_end = farthest

        return jump
        