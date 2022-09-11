class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prefix = [nums[0]]*len(nums)
        sufix = [nums[-1]]*len(nums)
        
        for i in range(1,len(nums)):
            prefix[i] = nums[i]*prefix[i-1] if prefix[i-1] != 0 else nums[i]
            
        for i in range(len(nums)-2, -1, -1):
            sufix[i] = nums[i]*sufix[i+1] if sufix[i+1] != 0 else nums[i]
        
        print(prefix, sufix)
        
        return max(sufix+prefix)