class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = [nums[0]]*len(nums)
        sufix = [nums[-1]]*len(nums)
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i] if prefix[i-1] != 0 else nums[i]
            
        for i in range(len(nums)-2, -1, -1):
            sufix[i] = sufix[i+1]*nums[i] if sufix[i+1] != 0 else nums[i]
        
        return max(sufix+prefix)


# EXPLANATION
# if we have an even number of -ve's we simply multiply all :)
# if we have odd number of -ve's we know that max prod will be on either sides of one of the -ve's
# if there is one 0 then the max prod is also either side of the 0
# if there are multiple 0's, the max prod will either be on each side of the zeros or between the zeros

# Overall we calculate the prefix and sufix sum with a small exception below
# if the our prefix becomes 0 we use 1 as prefix for the next calculations
# i.e if the prefix becomes 0 the next prefix will be the number there
# prefix[i-1] == 0 then prefix[i] = nums[i] instead of nums[i]*prefix[i-1] 
# (This will handle he between the zeros situation)