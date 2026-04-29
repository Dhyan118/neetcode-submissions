class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        # Helper array function 

        leftrow = [0] * n
        lowerdiog = [0] * (2*n - 1)
        upperdiog = [0] * (2*n - 1)

        def f(col):
            if col == n:
                res.append(["".join(row) for row in board])
                return 

            for row in range(n):
                if leftrow[row] == 0 and lowerdiog[row + col] == 0 and upperdiog[n-1+col-row] == 0:

                    board[row][col] = "Q"
                    leftrow[row] = 1
                    lowerdiog[row + col] = 1
                    upperdiog[n-1+col-row] = 1

                    # We are moving towards to next colum
                    f(col + 1)

                    # This is backtracking 

                    board[row][col] = "."
                    leftrow[row] = 0
                    lowerdiog[row + col] = 0
                    upperdiog[n-1+col-row] = 0

        f(0)
        return res
        