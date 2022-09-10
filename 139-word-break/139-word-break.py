class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False]*(len(s))
        dp[0] 
        
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i-(len(word)-1):i+1]:
                   
                    if i+1 == len(word):
                        dp[i] = True
                    elif dp[i-len(word)]:
                        dp[i] = dp[i-len(word)] 
        
        
        return dp[-1]
            
        
        
        
        
        
#         wordDict = set(wordDict)
#         self.res = False
#         self.maxLen = max([len(i) for i in wordDict])
        
#         def dfs(s):
            
#             if s == "":
#                 self.res = True
#                 return
            
#             for i in range(len(s)):
#                 if s[:i+1] in wordDict:
#                     dfs(s[i+1:])
                    
#         dfs(s)
        
#         return self.res
        
        
        
        
        
        
        
                    
        