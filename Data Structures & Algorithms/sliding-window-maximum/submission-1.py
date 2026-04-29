class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # store indices
        res = []

        for i in range(len(nums)):
            # remove indices out of window
            while q and q[0] <= i - k:
                q.popleft()

            # maintain decreasing order in deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # append max once window is full
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
