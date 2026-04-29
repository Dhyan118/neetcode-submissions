class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min heap will store: [distance, x, y]
        # Distance from origin = x^2 + y^2
        # We do not need sqrt because smaller x^2 + y^2 means closer point
        minHeap = []

        # Go through every point
        for x, y in points:
            
            # Calculate squared distance from origin (0,0)
            dist = x * x + y * y

            # Push distance and point into heap
            heapq.heappush(minHeap, [dist, x, y])

        # Store final k closest points
        res = []

        # Pop k times because heap always gives smallest distance first
        for i in range(k):
            
            # Remove closest point from heap
            dist, x, y = heapq.heappop(minHeap)

            # Add only [x, y] to answer
            res.append([x, y])

        return res