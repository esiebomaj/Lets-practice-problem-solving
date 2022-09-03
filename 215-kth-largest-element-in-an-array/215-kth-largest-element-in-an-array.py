import heapq

class Solution:
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kIdx = len(nums) - k
        def quickSelect(l, r):
            if l == r:
                return nums[l]
            
            pivot = nums[r]
            
            p = l
            
            for i in range(l,r):
                if nums[i]<=pivot:
                    # swap i with p
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
                    
            nums[p], nums[r] = nums[r], nums[p]
            
            if kIdx == p: return nums[p]
            elif kIdx > p: return quickSelect(p+1, r)
            else: return quickSelect(l, p-1)
            
        return quickSelect(0, len(nums)-1)
            
    
        