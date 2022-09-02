import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use the stones as a max heap
        # we multiply through by -1 to nable us use it as a max heap
        stones = [i*-1 for i in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            
            remainder = stone1 - stone2
            if remainder != 0:
                heapq.heappush(stones, remainder)
            
        
        if len(stones) == 1:
            # covert back to positive and return
            return stones[0]*-1
        else:
            return 0
        
        