class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
            
        prev2 , prev = cost[0], cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev, prev2)
            prev2, prev = prev, curr

        return min(prev, prev2)

