class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        nums = set(nums)
        res = 0
        for i in nums:
            if i in seen: continue
            seen.add(i)
            count = 1
            
            j = i
            while j - 1 in nums:
                j -= 1
                seen.add(j)
                count += 1
            
            j = i
            while j + 1 in nums:
                j += 1
                seen.add(j)
                count += 1
                
            res = max(res, count)
            
        return res 
            
            
            
            
            