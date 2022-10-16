import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        q = [(grid[0][0], 0, 0)]
        heapq.heapify(q)
        seen = set() # (rows and cols)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        N = len(grid)
        res = grid[0][0]
        
        while q:
            curr = heapq.heappop(q)
            if (curr[1], curr[2]) not in seen:
                seen.add((curr[1], curr[2]))
                res = max(res, curr[0])
                if curr[1] == N-1 and curr[2] == N-1:
                    return res
                for dy, dx in directions:
                    r,c = dy+curr[1], dx+curr[2]
                    if 0<=r<=N-1 and 0<=c<=N-1:
                        heapq.heappush(q, (grid[r][c], r, c))
        return res
                        
                
        
        
        