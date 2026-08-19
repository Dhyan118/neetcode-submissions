class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)

        count = 0

        for i in h:
            if i - 1 in h:
                continue
            curr_num = i
            curr_count = 1

            while curr_num + 1 in h:
                curr_num += 1
                curr_count += 1

            count = max(count, curr_count)

        return count

        