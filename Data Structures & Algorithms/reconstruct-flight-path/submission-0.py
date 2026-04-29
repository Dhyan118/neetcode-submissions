class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)  # Push destination into min-heap

        result = []  # This will store the final itinerary in reverse order

        # Step 2: Define DFS function
        def dfs(airport):
            # Explore all destinations from current airport
            while graph[airport]:
                next_dest = heapq.heappop(graph[airport])  # Always pick smallest lexicographically
                dfs(next_dest)
            result.append(airport)  # Add airport after exploring all paths (post-order)

        # Step 3: Start DFS from "JFK"
        dfs("JFK")

        # Step 4: Reverse the result to get correct order
        return result[::-1]