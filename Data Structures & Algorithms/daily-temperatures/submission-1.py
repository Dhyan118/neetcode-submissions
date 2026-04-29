class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # arr = [0]*len(temperatures)
        # for i in range(len(temperatures) - 1):
        #     if temperatures[i+1] > temperatures[i]:
        #         arr.append((i+1) - i)
        #     else:
        #         i+1
        # return arr
        

        arr = [0] * len(temperatures)
        stack = []  

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                a = stack.pop()
                arr[a] = i - a
            stack.append(i)

        return arr