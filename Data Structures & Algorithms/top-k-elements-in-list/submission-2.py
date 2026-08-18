class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = h.get(nums[i], 0) + 1 # make like freq Count
            
        sort_num = sorted(h, key = h.get, reverse = True) # Get exact freq in sorted order

        return sort_num[:k] # get Top value