class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            
            dp = [0]*(len(nums)+1)
            dp[0] = nums[0]
            
            for i in range(1, len(nums)):
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
                
            return dp[len(nums)-1]
        
        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))
        