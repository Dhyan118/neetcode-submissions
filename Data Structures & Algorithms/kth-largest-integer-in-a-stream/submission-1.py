class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # MinHeap with K largest integer 
        self.minHeap, self.k = nums, k # We have assign minheap as list 
        heapq.heapify(self.minHeap) # Now with this function we create minheap
        while len(self.minHeap) > k: # if the length of minHeap is grater than k
            heapq.heappop(self.minHeap) #then pop the min element 


    def add(self, val: int) -> int:
        # Add means push in the heap the value
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k: # if the length of minHeap is grater than k
            heapq.heappop(self.minHeap) #then pop the min element 

        return self.minHeap[0] # return first element as that will me kth largest elemnet
