class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        self.res = 0
        
        def bfs(r,c):
            q = [(r,c)]
            seen.add((r,c))
            area = 0
            
            while q:
                curr = q.pop()
                area += 1
                for dy, dx in [[1,0],[-1,0],[0,1],[0,-1]]:
                    i,j = curr[0]+dy, curr[1]+dx
                    
                    if (i,j) not in seen and 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                        seen.add((i,j))
                        q.insert(0, (i,j))
                                    
            self.res = max(self.res, area)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    # we have seen a new island
                    bfs(r,c)
                    
        return self.res
                    
        