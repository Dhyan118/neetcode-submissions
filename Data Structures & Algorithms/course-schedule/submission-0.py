class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build adjacency list and in-degree array
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            inDegree[a] += 1

        # Step 2: Initialize queue with all nodes having in-degree 0
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        # Step 3: Process nodes in topological order
        count = 0  # Count of courses processed
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in adj[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: If all courses processed, return True
        return count == numCourses

