class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        
        # Loop until pointers meet
        while left < right:
            # Calculate current area
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            
            # Update max area if current is larger
            max_area = max(max_area, area)
            
            # Move the pointer pointing to the shorter line
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area