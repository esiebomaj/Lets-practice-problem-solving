import heapq

class KthLargest:

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


# [4, 5, 8, 2]
# [2,3,4,4,5,5,8,9,10]