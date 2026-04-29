class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        j = [[] for i in range(len(nums)+ 1)]
        for v in nums:
            if v in h:
                h[v] += 1
            else:
                h[v] = 1
        for v,d in h.items():
            j[d].append(v)

        res= []
        for i in range(len(j) - 1, 0, -1):
            for n in j[i]:
                res. append (n)
                if len (res) == k:
                    return res


        