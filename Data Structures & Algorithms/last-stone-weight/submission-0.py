class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)

        while len(stones) > 1:

            first = max(stones)
            stones.remove(first)
            second = max(stones)
            stones.remove(second)

            if first != second:
                heapq.heappush(stones, first - second)
            else:
                pass

            heapq.heapify(stones)

        return stones[0] if stones else 0