class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # s = "babgbag", t = "bag"
        memo = {}
        def dfs(i,j):
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if j >= len(t):
                return 1
            
            if i >= len(s):
                return 0
            
            
            if s[i] == t[j]:
                rt = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                rt = dfs(i+1, j) 
                
            memo[(i,j)] = rt
            return rt
            
        return dfs(0,0)
            
        