class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Helper function to add valid cells to the queue
        def addCell(r, c):
            # Check boundaries and if the cell is fresh
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 2       # make it rotten
                q.append((r, c))
                nonlocal fresh     # add to queue
                fresh -= 1           # one less fresh fruit

        # Step 1: Initialize queue with all rotten fruits and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # If no fresh fruits, return 0 immediately
        if fresh == 0:
            return 0

        # Step 2: BFS traversal
        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                # Try to rot all 4 adjacent cells
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            # After processing one full layer, increment time
            minutes += 1

        # Step 3: If fresh fruits remain, return -1
        return minutes if fresh == 0 else -1