class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def isPalindrome(sub):
            return sub == sub[::-1]

        def f(index, path):
            # base case: reached end of string
            if index == n:
                res.append(path[:])
                return

            # loop from current index to end
            for i in range(index, n):
                substring = s[index:i + 1]
                # check if substring is palindrome
                if isPalindrome(substring):
                    path.append(substring)
                    f(i + 1, path)  # recurse for remaining string
                    path.pop()      # backtrack

        f(0, [])
        return res