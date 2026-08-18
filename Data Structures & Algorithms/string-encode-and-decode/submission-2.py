class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1

            word = s[start:start + length]

            res.append(word)

            i = start + length

        return res          
