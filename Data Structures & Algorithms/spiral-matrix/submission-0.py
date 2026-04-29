class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # we have to traverse like spring in matrix
        res = []
        while matrix:
            # Add top row
            res += matrix.pop(0)
            # Add right column
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            # Add bottom row
            if matrix:
                res += matrix.pop()[::-1]
            # Add left column
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res