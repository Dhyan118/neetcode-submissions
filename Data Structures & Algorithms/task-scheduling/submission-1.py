class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        #any value store in maxheap is always -ve
        maxHeap = [-ct for ct in count.values()]
        # heapify can convert array to heap 
        heapq.heapify(maxHeap) 
        time = 0

        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:

                ct = 1 + heapq.heappop(maxHeap)
                if ct:
                    q.append((ct,  time + n))

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

        

