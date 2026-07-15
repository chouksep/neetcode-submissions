class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        output = float("inf")
        i = 0
        while (i + k - 1) < len(nums):
            output = min(output, (nums[i+k-1] - nums[i]))
            i += 1
        return output

        
        




        


        