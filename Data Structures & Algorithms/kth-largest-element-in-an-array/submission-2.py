class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            # Keep only k largest elements in heap
            if len(heap) > k:
                heapq.heappop(heap)

        # Step 2: The root of the heap is the kth largest element
        return heap[0]
        