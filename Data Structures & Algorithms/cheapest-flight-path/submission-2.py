class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
         # build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # min-heap: (cost so far, current node, stops used)
        heap = [(0, src, 0)]
        
        # track best [node][stops] cost
        visited = dict()
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            
            # if destination reached
            if node == dst:
                return cost
            
            # if stops exceed limit, skip
            if stops > k:
                continue
            
            # avoid revisiting with worse cost
            if (node, stops) in visited and visited[(node, stops)] <= cost:
                continue
            visited[(node, stops)] = cost
            
            # explore neighbors
            for nei, price in graph[node]:
                new_cost = cost + price
                heapq.heappush(heap, (new_cost, nei, stops + 1))
        
        return -1