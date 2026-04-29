class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix), len(matrix[0])

        l , r = 0 , rows * cols -1

        while l <= r:
            mid = (l + r) // 2

            # Convert 1D array to 2D matrix

            row = mid // cols
            c = mid % cols

            if matrix[row][c] == target:
                return True
            elif matrix[row][c] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
