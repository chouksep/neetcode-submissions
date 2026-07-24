class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix = [1, 1, 2, 8] if i == 0 --> skip
        suffix = [48, 24,6,1] if i == n-1 --> skip
        """
        
        n = len(nums)
        output = [1]*n

        for i in range(1,n):
            output[i] = output[i-1] * nums[i-1]
        
        postfix = 1

        for j in range(n-1,-1, -1):
            output[j] = output[j] * postfix
            postfix *= nums[j]
        return output
