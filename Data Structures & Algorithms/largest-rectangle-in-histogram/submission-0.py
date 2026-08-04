class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """


        i = 5, start = 4, height = 4, stack = [(0,1), (2, 2)], idx = 4, h = 2, output = 7
        
                
        """
        stack = [] # (start_index, height)
        temp_area = 0
        output = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                
                idx, h = stack.pop()
                output =  max((h * (i-idx)), output)
                start = idx
            stack.append((start, height))
        
        for idx, h in stack:
            output = max(output, h*(len(heights)-idx))
            
        return output