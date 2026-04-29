class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_res = 0

        for i in range(n):
            left_max = max(height[:i+1])

            right_max = max(height[i:])
            # Min of left and right height and - with height at which current we are standing
            total_res += min(left_max, right_max) -height[i]

        return total_res