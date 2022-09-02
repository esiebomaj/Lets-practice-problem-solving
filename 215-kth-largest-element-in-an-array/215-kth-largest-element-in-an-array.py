class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums) #O(NlogN)
        return nums[-k]
    
        