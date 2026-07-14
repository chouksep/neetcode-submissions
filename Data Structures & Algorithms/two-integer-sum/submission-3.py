class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_diff = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_diff:
                return [prev_diff[diff], i]
            prev_diff[n] = i

        