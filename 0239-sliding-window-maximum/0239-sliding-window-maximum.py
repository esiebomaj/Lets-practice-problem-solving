import heapq 
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []
        for i in range(k):
            val = nums[i]
            while window and window[-1][1] < val:
                window.pop()
            window.append((i, val))
        
        res.append(window[0][1])
            
        l = 1
        r = k
        
        while r < len(nums):
            
            while window and window[0][0] < l:
                window.popleft()
            val = nums[r]
            while window and val > window[-1][1]:
                window.pop()
            window.append((r, val))
            
            res.append(window[0][1])
            
            l += 1
            r += 1
        
        return res
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         l = 0
#         r = k
#         window = deque(nums[:r])
#         res = []
#         res.append(max(window))
        
#         while r < len(nums):
#             # remove l
#             window.popleft()
#             window.append(nums[r])

#             res.append(max(window))
            
#             l += 1
#             r += 1
            
#         print(res)
#         return res
        
            
        