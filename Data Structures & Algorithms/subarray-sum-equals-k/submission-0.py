class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = defaultdict(int)
        h[0] = 1

        curr_sum = 0
        count = 0

        for i in nums:
            curr_sum += i
            count += h[curr_sum - k]
            h[curr_sum] += 1

        return count