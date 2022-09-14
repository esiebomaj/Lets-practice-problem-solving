class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}
        
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            isMatch = (i < len(s) and j < len(p)) and (s[i] == p[j] or p[j] == ".")
            
            if j+1 < len(p) and p[j+1] == "*":
                rt = dfs(i, j+2) or (isMatch and dfs(i+1, j))
            else:
                rt = isMatch and dfs(i+1, j+1)
            
            memo[(i,j)] = rt
            return rt
            
        return dfs(0,0)