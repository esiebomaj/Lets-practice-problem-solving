from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        q = deque([(0,0)])
        seen = set()
        seen.add(0)
        
        while q:
            id, lvl = q.pop()
            seen.add(id)
            for j in range(1, nums[id]+1):
                i = id + j
                if i not in seen:
                    if i == len(nums)-1:
                        return lvl+1
                    seen.add(i)
                    q.appendleft((i, lvl+1))
            
            
        
        