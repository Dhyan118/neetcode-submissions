class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = set()
        l = 0
        count = 0
        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l]) # Remove this element from first and increment the lefft pointer
                l += 1
            h.add(s[r])
            count = max(count, r - l + 1)
        return count