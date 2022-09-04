class MedianFinder:

    def __init__(self):
        self.maxheap, self.minheap = [], []

    def addNum(self, num: int) -> None:
        if self.maxheap and num > -self.maxheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
            
        if len(self.maxheap) > len(self.minheap)+1:
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)
        if len(self.minheap) > len(self.maxheap)+1:
            val = -heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, val)
        
        

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return ((-self.maxheap[0]) + self.minheap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()