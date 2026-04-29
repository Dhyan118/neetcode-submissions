class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n

        for i in range(1, m):
            temp = [1] * n
            for j in range(1, n):

                temp[j] = prev[j] + temp[j - 1]

            prev = temp

        return prev[-1]
        
        