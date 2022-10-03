class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #METHOD 1
        res = sum(range(len(nums)+1))
        for i in nums:
            res -= i
            
        return res
        
        # METHOD 2
        res = 0
        for i in range(len(nums)+1):
            res = res ^ i
        for i in nums:
            res = res ^ i
        return res