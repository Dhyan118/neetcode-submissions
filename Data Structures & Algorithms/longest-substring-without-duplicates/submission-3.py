class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = set()
        l = 0
        max_res = 0

        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l += 1

            h.add(s[r])
            max_res = max(max_res, r - l + 1)

        return max_res