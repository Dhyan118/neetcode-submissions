class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = Counter(nums)

        heap = []

        for i, count in h.items():
            heapq.heappush(heap, (count, i))

            if len(heap) > k:
                heapq.heappop(heap)

        return [i for count, i in heap]