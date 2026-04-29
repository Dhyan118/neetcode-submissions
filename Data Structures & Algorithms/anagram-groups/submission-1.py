class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for i in range(len(strs)):
            check = ''.join(sorted(strs[i]))
            if check in h:
                h[check].append(strs[i])
            else:
                h[check]= [strs[i]]
        return list(h.values())
        