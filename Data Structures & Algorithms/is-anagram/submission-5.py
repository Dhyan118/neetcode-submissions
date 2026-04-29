class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c = [0] * 26
        for i in range(len(s)):
            c[ord(s[i]) - ord('a')] += 1
            c[ord(t[i]) - ord('a')] -= 1
        
        for val in c:
            if val != 0:
                return False
        return True

        