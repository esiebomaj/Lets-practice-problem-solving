import heapq

class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     nums = sorted(nums) #O(NlogN)
    #     return nums[-k]
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
    
        