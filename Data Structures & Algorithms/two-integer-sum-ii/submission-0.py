class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        #curr_sum = 0
        while l < r:

            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l+1,r+1]
            elif curr_sum < target:
                l += 1
            else: 
                r -=1
        return []
        
        # for l in range(len(numbers)):
        #     if numbers[l] + numbers[r] == target:
        #         reasult.append(l+1,r)
        #     else:
        #         l +=1
        # return reasult