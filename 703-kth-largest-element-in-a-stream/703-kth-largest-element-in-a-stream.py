import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        
        for i in range(len(nums)-k):
            heapq.heappop(self.heap)
        
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        for i in range(len(self.heap) - self.k):
            heapq.heappop(self.heap)
        
        return self.heap[0]
        

# [4, 5, 8, 2] [2,4,4,5,5,8,9,10]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)