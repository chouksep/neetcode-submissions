class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        """
        Brute force: At every index, extract window of size k, iterate through each element in the window to find max and update list when found. Time complexity : O (n*k) space complexity : O(number of window possible between left and right edge)
        Given constraints, worst case can be O(n2) when k == nums.length --> 10,000,000,000  10 billion operations not feasible

        Here from the example, I observe two consequent window have overlapping element, so at each index in brute force, we are duplicating checking of that element, we are only concerned with the new element added and old element deleted
        when updating the max integer list
        """

        l = 0
        max_list = []
        curr_window_max = deque([])
        for r in range(len(nums)):
            
            while curr_window_max and nums[curr_window_max[-1]] < nums[r]:
                curr_window_max.pop()
            curr_window_max.append(r)

            if r - l + 1 == k:
                max_list.append(nums[curr_window_max[0]])
                l += 1
                if curr_window_max and l > curr_window_max[0]:
                    curr_window_max.popleft()
                
        return max_list