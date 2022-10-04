class Solution:
    def checkValidString(self, s: str) -> bool:
        # Greedy method
        minCount, maxCount = 0, 0
        for i in s:
            if i == "(":
                minCount, maxCount = minCount+1, maxCount+1
            elif i == ")":
                minCount, maxCount = minCount-1, maxCount-1
            elif i == "*":
                minCount, maxCount = minCount-1, maxCount+1
                
            if maxCount < 0:
                return False
            
            if minCount < 0:
                minCount = 0
                
        return minCount <= 0 <= maxCount
    # ( * ) (
        
        
        # recursion and memoization solution
        memo = {}
        def dfs(i, count):
            
            if (i,count) in memo:
                return memo[(i, count)]
            
            if i >= len(s):
                return count == 0
            
            if count < 0:
                return False
                
            
            if s[i] == "(":
                memo[(i, count)] = dfs(i+1, count+1)
                return memo[(i, count)]
                
            elif s[i] == ")":
                memo[(i, count)] = dfs(i+1, count-1)
                return memo[(i, count)]
            elif s[i] =="*":
                memo[(i, count)] = dfs(i+1, count+1) or dfs(i+1, count-1) or dfs(i+1, count)
                return memo[(i, count)]
            
        return dfs(0,0)