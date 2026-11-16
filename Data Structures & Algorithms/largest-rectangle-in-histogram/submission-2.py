class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack  = []
        max_size = -1
        # 2 1 5 6 2 3 
        for (i,h) in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:

                area = (i - stack[-1][0]) * stack[-1][1]
                max_size = max(max_size, area)
                start = stack[-1][0]
                stack.pop()

            stack.append((start, h))
        height = len(heights)
        for (idx, h) in stack:
            max_size = max(max_size, (height - idx )  * h)
     
        return max_size

