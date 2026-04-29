class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j=len(heights)-1
        maxx=0
        i=0
        while i < j:
            a = min(heights[i], heights[j])*(j-i)
            maxx = max(a, maxx)
            if heights[i] < heights[j]:
                i += 1           
            else:           
               j-=1
        return maxx
    