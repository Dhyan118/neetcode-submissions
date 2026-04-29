class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pac = set()
        alt = set()

        def dfs(r, c, vist, prev_height):
            if ((r,c) in vist or r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prev_height):
                return

            vist.add((r, c))

            dfs(r + 1, c, vist, heights[r][c])
            dfs(r - 1, c, vist, heights[r][c])
            dfs(r, c + 1, vist, heights[r][c])
            dfs(r, c - 1, vist, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, alt, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, alt, heights[r][cols - 1])

        res = list(pac & alt)
        return res
