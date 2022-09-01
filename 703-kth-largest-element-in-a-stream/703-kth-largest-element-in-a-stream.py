import heapq

class KthLargest:
    # we use a min head (priority q) of len k to keep track of the value
    # after adding a value we ensure that the heap is of size k by using a while loop and heappop
    # this way the heapq contains the k largest values
    # and the k largest value is the smallest value in the heap i.e heap[0]

    def __init__(self, k: int, nums: List[int]):
        print(nums)
        heapq.heapify(nums)
        self.k = k
        while len(nums) > self.k:
            heapq.heappop(nums)
        
        self.nums = nums
        print(nums)
             
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
            
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)