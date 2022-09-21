class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        currSum = 0
        maxSum = float(-inf)
        
        for num in nums:
            if num+currSum < num:
                currSum = num
            else:
                currSum = currSum + num
                
            maxSum = max(maxSum, currSum)
            
        return maxSum
        