class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols = len(grid[0])
        q=[]
        seen = set()
        oranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 or grid[r][c] == 2:
                    oranges+=1
                if grid[r][c]==2:
                    q.insert(0, (r,c, 0))
                    seen.add((r, c))
                    
                    
        print(q)
        
        mins = 0
        
        while q:
            curr = q.pop()
            mins = max(mins, curr[2])
            for dy, dx in [[1,0], [-1,0], [0,1], [0,-1]]:
                i,j = curr[0]+dy, curr[1]+dx
                if (i,j) not in seen and 0<=i<rows and 0<=j<cols and grid[i][j] == 1:
                    q.insert(0, (i,j,curr[2]+1))
                    seen.add((i,j))
        
        if oranges == len(seen):
            return mins
        return -1
    
    # [[2,1,1]
    #  [0,1,1]
    #  [1,0,1]]
                    