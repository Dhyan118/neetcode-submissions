# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         h = {}
#         counter = 0
#         for i in range(len(nums)):
#             if nums[i] + 1 == nums[i+1]:
#                 h.append()
#             else:


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #h=[0,3,2,5,4,6,1]
        #nums=[0,3,2,5,4,6,1,1]
        h = set(nums)
        output = 0

        for v in h:
            if (v - 1) not in h:
                counter = 1
                while (v + counter) in h:
                    counter += 1
                output = max(counter, output)
        return output
        




        # if not nums:
        #     return 0
        # if len(nums) ==1:
        #     return 1
        # nums.sort()
        # output =1 
        # counter = 1
        # print(nums)
        # for i in range(1,len(nums)):
        #     print(nums[i])
        #     if nums[i-1]+1 == nums[i]:
        #         counter +=1
        #     elif nums[i] != nums[i-1]:
        #         output = max(counter,output)
        #         counter = 1
        # return max(counter,output)



        