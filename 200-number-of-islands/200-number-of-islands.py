class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        self.islandCount = 0
        
        def bfs(r,c):
            
            q = [(r,c)]
            self.islandCount += 1

            while q:
                curr = q.pop()
                i,j = curr
                seen.add((i,j))

                for dx, dy in [[1,0], [-1,0], [0,1],[ 0,-1]]:
                    i,j = dx+curr[0], dy+curr[1]

                    if  i >= 0 \
                    and i < rows \
                    and j >= 0 \
                    and j < cols \
                    and grid[i][j] == "1" \
                    and (i,j) not in seen:
                        seen.add((i,j))
                        q.insert(0, (i,j))
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:

                    bfs(r,c)
                    
                                
                
        return self.islandCount
                                
                        
        