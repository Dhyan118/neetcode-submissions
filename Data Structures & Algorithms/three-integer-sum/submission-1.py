class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        target=0 
        a = []
        # print(nums)
      
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=len(nums) - 1
            while j<k:
                curr_value = nums[i]+nums[j]+nums[k]
                if curr_value> target:
                    k -=1
                elif curr_value < target:
                    j += 1
                else:
                    a.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
        return a
        