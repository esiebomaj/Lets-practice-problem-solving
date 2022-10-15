class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        
        for i,h in enumerate(heights):
            prevId = i
            while stack and h < stack[-1][1]:
                prevId, prevH = stack.pop()
                res = max(res, prevH * (i-prevId))
                
            stack.append((prevId, h))
        
        for i,h in stack:
            res = max(res, h * (len(heights)-i))
            
        return res
                
        