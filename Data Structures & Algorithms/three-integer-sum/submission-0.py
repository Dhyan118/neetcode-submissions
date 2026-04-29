class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        target=0 
        a = []
      
        for i in range(len(nums)-1):
            j = i+1
            k=len(nums) - 1
            while j < k:
                curr_value = nums[i]+nums[j]+nums[k]
                if curr_value < target:
                    j +=1
                elif curr_value > target:
                    k-=1
                else:
                    a.append([nums[i],nums[j],nums[k]])
                    j +=1
                    k -=1
        zeke = set(tuple(sub) for sub in a)
        return [list(t) for t in zeke]
        