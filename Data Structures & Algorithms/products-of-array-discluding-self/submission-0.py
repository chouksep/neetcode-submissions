class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix = [1, 1, 2, 8] if i == 0 --> skip
        suffix = [48, 24,6,1] if i == n-1 --> skip
        """
        
        prefix_lst = []
        prefix = 1

        for i in range(len(nums)):
            if i == 0:
                prefix_lst.append(1)
            else:
                prefix *= nums[i-1]
                prefix_lst.append(prefix)

        suffix_lst = []
        suffix = 1

        for j in range(len(nums)-1, -1, -1):
            if j == len(nums)-1:
                suffix_lst.append(1)

            else:
                suffix *= nums[j+1]
                suffix_lst.append(suffix)

        output = []
        for k in range(len(nums)):
            output.append(prefix_lst[k] * suffix_lst[len(nums) - k -1])
        return output
