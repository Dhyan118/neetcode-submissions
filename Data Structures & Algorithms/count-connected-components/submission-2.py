class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        size =[[] for _ in range(n)]
        parent =[[] for _ in range(n)]

        for i in range(n):
            size[i] = 1
            parent[i] = i

        def find(node):
            if parent[node] == node:
                return node
            ancester = find(parent[node])
            parent[node] = ancester
            return ancester

        def union(u, v):
            p_u = find(u)
            p_v = find(v)
            if (p_u == p_v):
                return False

            if (size[p_u] >= size[p_v]):
                size[p_u] += size[p_v]
                parent[p_v] = p_u
            else:
                size[p_v] += size[p_u]
                parent[p_u] = p_v
            return True

        for edge in edges:
            u = edge[0]
            v = edge[1]

            if union(u, v) == True:
                n -= 1
        return n
            
