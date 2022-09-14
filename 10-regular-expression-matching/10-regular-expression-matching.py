class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        def dfs(i,j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            isMatch = (i < len(s) and j < len(p)) and (s[i] == p[j] or p[j] == ".")
            
            if j+1 < len(p) and p[j+1] == "*":
                return dfs(i, j+2) or (isMatch and dfs(i+1, j))
            else:
                return isMatch and dfs(i+1, j+1)
            
        return dfs(0,0)
    
        
        # s = "ab" 
        i = 2
        
        p = ".*c"
        j = 0