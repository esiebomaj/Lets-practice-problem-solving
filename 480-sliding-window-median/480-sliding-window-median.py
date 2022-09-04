class Solution:
    def balanceHeaps(self,):
        if len(self.maxheap) > len(self.minheap)+1:
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)
        elif len(self.minheap) > len(self.maxheap):
            val = -heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, val)
            
    def addValue(self, val):
        if self.maxheap and val > -self.maxheap[0]:
            # add to self.minheap
            heapq.heappush(self.minheap, val)
        else:
            # add to maxheap
            heapq.heappush(self.maxheap, -val)
    
    def remove(self, heap, val):
        pos = heap.index(val)
        heap[pos] = heap[-1]
        del heap[-1]

        if pos < len(heap):
            heapq._siftup(heap, pos)
            heapq._siftdown(heap, 0, pos)
    
    def calculateMedian(self,):
        if len(self.maxheap)>len(self.minheap):
            self.res.append(-self.maxheap[0])
        elif len(self.minheap) > len(self.maxheap):
            self.res.append(self.minheap[0])
        else:
            self.res.append(((-self.maxheap[0])+self.minheap[0])/2)
            
        
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        self.maxheap, self.minheap = [], []
        for i in range(k):
            self.addValue(nums[i])
            self.balanceHeaps()

        l = 0
        r = k
        self.res = []
        while r < len(nums):
            # step 1: calculate the curr median
            self.calculateMedian()
            
            # step 2: add the value at r
            self.addValue(nums[r])
            self.balanceHeaps()            
            
            # step 3: remove the value at l
            if nums[l] > -self.maxheap[0]:
                self.remove(self.minheap, nums[l])
            else:
                self.remove(self.maxheap, -nums[l])
            self.balanceHeaps()
            
            # increment l and r
            l += 1
            r += 1
            
        self.calculateMedian()
        return self.res
    
    
    
    
    
    
    
# res = [1,2]
# [1,2,3,4,5,6,7,8]
# maxheap = [2]                minheap=[3]
    
    
    
    
    
    
    
    
    
        