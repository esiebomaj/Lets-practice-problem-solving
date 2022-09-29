class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacSeen = set()
        atlSeen = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        def dfs(r,c, visited):
            if (r,c) in visited:
                return
            
            visited.add((r,c))
            
            for dy,dx in directions:
                i,j = dy+r, dx+c
                if 0 <= i < rows and 0 <= j < cols and heights[r][c] <= heights[i][j]: 
                    dfs(i,j,visited)
        
            
        for r in range(rows):
            dfs(r, 0, pacSeen)
            dfs(r, cols-1, atlSeen)
        
        for c in range(cols):
            dfs(0, c, pacSeen)
            dfs(rows-1, c, atlSeen)
        
        res = []
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlSeen and (r,c) in pacSeen:               
                    res.append((r,c))
                
        return res