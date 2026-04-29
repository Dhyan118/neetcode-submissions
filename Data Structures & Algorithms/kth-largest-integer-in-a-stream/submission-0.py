class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        # If heap exceeds size k, remove smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # The smallest element in the heap is the kth largest overall
        return self.minHeap[0]
        
