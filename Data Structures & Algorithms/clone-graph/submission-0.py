"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Craete a dictionary to map original nodes to their cloned copies 

        h = {}

        def dfs(curr):

            if curr in h:
                return h[curr]

            copy = Node(curr.val)
            h[curr] = copy

            for i in curr.neighbors:
                copy.neighbors.append(dfs(i))

            return copy

        return dfs(node)

        