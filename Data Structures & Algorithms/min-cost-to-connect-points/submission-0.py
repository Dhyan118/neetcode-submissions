class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Step 1: Get the number of points
        n = len(points)

        # Step 2: Keep track of which points are already connected (visited)
        visited = set()

        # Step 3: Create a min-heap (priority queue)
        # Each element in the heap will be a tuple (cost, point_index)
        # Start from point 0 with cost 0
        min_heap = [(0, 0)]

        # Step 4: Initialize total cost to 0
        total_cost = 0

        # Step 5: Run until we have connected all points
        while len(visited) < n:
            # Pop the smallest cost edge from the heap
            cost, i = heapq.heappop(min_heap)

            # If this point is already connected, skip it
            if i in visited:
                continue

            # Otherwise, include this point in the MST
            total_cost += cost
            visited.add(i)

            # Step 6: For the newly added point, calculate the cost to connect
            # it to all other unvisited points
            for j in range(n):
                if j not in visited:
                    # Extract coordinates
                    x1, y1 = points[i]
                    x2, y2 = points[j]

                    # Manhattan distance between point i and j
                    dist = abs(x1 - x2) + abs(y1 - y2)

                    # Push this edge into the heap
                    heapq.heappush(min_heap, (dist, j))

        # Step 7: Once all points are connected, return the total cost
        return total_cost

        