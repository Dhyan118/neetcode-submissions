class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python has min heap so we put -ve value
        # into the list and then convet to heap
        stones = [-s for s in stones]
        heapq.heapify(stones) # We created the heap and put the stones into it

        while len(stones) > 1:

            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # first = -8
            # second = -7

            if second > first:
                heapq.heappush(stones, first - second)
                # -8 -(-7) = -1
        stones.append(0) # if dont have negative value then we will put zero as answer
            
        return abs(stones[0])
