class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)

        for i in strs:
            key = ''.join(sorted(i))

            h[key].append(i)

        return list(h.values())