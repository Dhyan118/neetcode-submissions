class Solution:
    def isValid(self, s : str) -> bool:
        Stack = []
        opentoclose = { ")":"(", "}":"{","]":"["}

        for c in s:
            if c in opentoclose:
                if Stack and Stack[-1] == opentoclose[c]:
                    Stack.pop()
                
                else:
                    return False
            else:
                Stack.append(c)

        return True if not Stack else False
