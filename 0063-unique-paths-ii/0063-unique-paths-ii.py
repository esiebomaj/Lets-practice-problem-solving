class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Space complexity is O(1)
        # I could consider creating another matrix for my computation
        # but that would make the space O(N*M)
        
        # Time complexity is O(N*M)
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        first = obstacleGrid[0][0]
        obstacle = False
        for r in range(n):
            if obstacleGrid[r][0] == 1:
                obstacle = True
            if obstacle == True:
                obstacleGrid[r][0] = 0
            else:
                obstacleGrid[r][0] = 1
            
        obstacle = False
        for c in range(1,m):
            if obstacleGrid[0][c] == 1 or first == 1:
                obstacle = True
            if obstacle == True:
                obstacleGrid[0][c] = 0
            else:                
                obstacleGrid[0][c] = 1
            
        for r in range(1,n):
            for c in range(1,m):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
                    
        return obstacleGrid[-1][-1]
            
            
                
            
        