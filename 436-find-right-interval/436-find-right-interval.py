import heapq

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        minstart = [(interval[0], interval[1], i) for i,interval in enumerate(intervals)]
        
        minstop = [(interval[1], interval[0], i) for i,interval in enumerate(intervals)]
        
        
        heapq.heapify(minstart)
        heapq.heapify(minstop)
        
        res = [-1]*len(intervals)

        while minstop:
            # print("minstart", minstart)
            # print("minstop", minstop)
            curr = heapq.heappop(minstop)
            
            while minstart and (minstart[0][0] < curr[0]):
                heapq.heappop(minstart)
            
            if minstart:
                idx = curr[2]
                res[idx] = minstart[0][2]
                
        # print(res)
        return res
            
                