class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        for i in range(1, len(nums)):
            if nums[i-1] == 0:
                return False
            nums[i] = max(nums[i-1]-1, nums[i])
            
        return True
        