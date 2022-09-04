import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxheap, minheap  = [], []
        #  maxheap (p,c), minheap (c,p) 
        
        for c,p in zip(capital, profits):
            heapq.heappush(minheap, (c,p))
        
        while k > 0:
            
            while minheap and w >= minheap[0][0]:
                c,p = heapq.heappop(minheap)
                heapq.heappush(maxheap, (-p,c))
            
            if maxheap:
                p,c = heapq.heappop(maxheap)
                w = w -p
                
            k -= 1
            
        return w
        
        