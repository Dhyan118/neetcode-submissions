class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
    # Step 1: Calculate the prefix products
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
    
    # Step 2: Calculate the postfix products
        postfix = [1] * n
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
    
    # Step 3: Multiply prefix and postfix products at each index
            result = [prefix[i] * postfix[i] for i in range(n)]
    
        return result


