class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        # we take two hash map 
        countS, countT = {}, {}

        #count the freq of each character 
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)
