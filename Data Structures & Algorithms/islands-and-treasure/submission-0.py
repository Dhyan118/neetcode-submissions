class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()      # keeps track of visited cells
        q = deque()        # queue for BFS

        # Helper function to add a valid room to the queue
        def addRoom(r, c):
            # If out of bounds, already visited, or wall, skip
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                (r, c) in visit or grid[r][c] == -1):
                return
            # Mark as visited and add to queue
            visit.add((r, c))
            q.append((r, c))

        # Step 1: Add all gates (0s) to the queue first
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        # Step 2: BFS traversal from all gates simultaneously
        dist = 0
        while q:
            # Process all cells at the current distance level
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist  # update distance for this cell

                # Explore 4 directions
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            # After finishing one BFS level, increment distance
            dist += 1

        