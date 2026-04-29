class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        h = defaultdict(list)

        for a, b in edges:
            h[a].append(b)
            h[b].append(a)

        vist = set()
        count = 0

        def dfs(node):
            for j in h[node]:
                if j not in vist:
                    vist.add(j)
                    dfs(j)

        for i in range(n):
            if i not in vist:
                vist.add(i)
                dfs(i)
                count += 1

        return count

        