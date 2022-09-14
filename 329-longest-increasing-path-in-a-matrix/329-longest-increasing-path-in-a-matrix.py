class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        
        def dfs(r, c, prev):
            
            if r >= len(matrix) or c >= len(matrix[0]) or r < 0 or c < 0 or matrix[r][c] <= prev:
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            prev = matrix[r][c]
            
            
            rt = float(-inf)
            for (i,j) in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                rt = max(rt, 1 + dfs(r+i, c+j, prev))
            
            memo[(r,c)] = rt
            return rt
        
        res = float(-inf)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, dfs(r, c, float(-inf)))
        
        return res