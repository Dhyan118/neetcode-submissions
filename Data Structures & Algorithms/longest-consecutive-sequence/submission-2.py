class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) ==1:
            return 1
        nums.sort()
        output =1 
        counter = 1
        print(nums)
        for i in range(1,len(nums)):
            print(nums[i])
            if nums[i-1]+1 == nums[i]:
                counter +=1
            elif nums[i] != nums[i-1]:
                output = max(counter,output)
                counter = 1
        return max(counter,output)
        