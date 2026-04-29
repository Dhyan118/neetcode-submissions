class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        prev2 , prev = cost[0], cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev, prev2)
            prev2, prev = prev, curr

        return min(prev, prev2)

