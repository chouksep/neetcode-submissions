class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        last_seen = {}

        for i in range(len(nums)):
            if (nums[i] in last_seen) and (abs(i-last_seen[nums[i]]) <= k):
                return True
            
            last_seen[nums[i]] = i # update the most recent index
        return False
            



        