class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Initialize parent and rank arrays
        parent = [i for i in range(n)]  # Each node is its own parent initially
        rank = [1] * n                  # Rank helps keep the tree flat

        # Step 2: Define the find function with path compression
        def find(node):
            # If node is not its own parent, recursively find the root
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        # Step 3: Define the union function with union by rank
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            # If they already have the same root, they are in the same component
            if rootA == rootB:
                return False  # No merge happened

            # Attach smaller ranked tree under larger ranked tree
            if rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            elif rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            else:
                parent[rootB] = rootA
                rank[rootA] += 1  # Increase rank if both have same rank

            return True  # Merge happened

        # Step 4: Start with n components (each node is its own)
        components = n

        # Step 5: For each edge, union the two nodes
        for a, b in edges:
            # If a and b are merged successfully, reduce component count
            if union(a, b):
                components -= 1

        # Step 6: Return the number of connected components
        return components

        