class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = -1
        for idx in range(len(heights)):
            start = idx
            while stack and stack[-1][1] > heights[idx]:
                (lid , lit) = stack.pop()
                max_area = max( (idx - lid) * lit, max_area)
                start = lid
            stack.append((start, heights[idx]))
            
        
        for (idx, h) in stack:
            max_area = max(max_area, (len(heights) - idx) * h)
        return max_area

