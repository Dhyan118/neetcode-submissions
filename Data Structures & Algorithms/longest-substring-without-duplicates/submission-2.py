class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
       # Time Complexity : O(n) 
       # Space Complexity : O(M) 
        h = set()
        l =  0
        count = 0
        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l += 1
            h.add(s[r])
            count = max(count, r-l+1)
        return count
        