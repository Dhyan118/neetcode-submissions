class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        max_area = 0

        def dfs(r, c):
            if(r<0 or c<0 or r >= row or c >= col or grid[r][c] == 0):
                return 0
            area = 1
            grid[r][c] = 0
            area+=dfs(r + 1, c)
            area+=dfs(r - 1, c)
            area+=dfs(r, c + 1)
            area+=dfs(r, c - 1)

            return area 
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)

        return max_area
