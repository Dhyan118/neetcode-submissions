class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        h =[]
        for i in tokens:
            if i in ("+","-","*","/"):
                b = int(h.pop())
                a = int(h.pop())
                if i == "+":
                    h.append(a+b)
                elif i == "-":
                    h.append(a-b)
                elif i == "*":
                    h.append(a*b)
                else:
                    h.append(int(a/b))
            else:
                h.append(int(i)) 
        return int(h.pop())                    
            
        
        