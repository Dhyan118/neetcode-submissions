class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Step 1: Initialize two pointers
        left, right = 0, len(numbers) - 1

        # Step 2: Move pointers until they meet
        while left < right:
            # Calculate current sum of two pointers
            curr_sum = numbers[left] + numbers[right]

            # If the sum matches target, return 1-indexed positions
            if curr_sum == target:
                return [left + 1, right + 1]

            # If current sum is smaller, move left pointer to increase sum
            elif curr_sum < target:
                left += 1

            # If current sum is larger, move right pointer to decrease sum
            else:
                right -= 1

        # Step 3: Problem guarantees one valid solution, so no need for fallback
        return []

