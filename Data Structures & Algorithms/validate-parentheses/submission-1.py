class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h = {")":"(", "}":"{", "]":"["}

        for i in s:
            if i in h:
                if stack and stack[-1] == h[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
