class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {(len(s), 0): True}
        def dfs(i, count):
            if i == len(s):
                return count == 0
            if count < 0:
                return False
            
            if (i, count) in memo:
                return memo[(i,count)]
            
            
            if s[i] == "(":
                rt = dfs(i+1, count+1)
                memo[(i,count)] = rt
                return rt
            
            if s[i] == ")":
                if count > 0: 
                    rt = dfs(i+1, count-1)
                    memo[(i,count)] = rt
                    return rt
                else:
                    memo[(i,count)] = False
                    return False
            
            if s[i] == "*":
                rt = dfs(i+1, count) or dfs(i+1, count+1) or dfs(i+1, count-1)
                memo[(i,count)] = rt
                return rt
                
            return rt
        
        return dfs(0, 0)