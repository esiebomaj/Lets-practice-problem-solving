class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        
        for r in range(len(word2)+1):
            dp[r][0] = r
        for c in range(len(word1)+1):
            dp[0][c] = c
        
        for r in range(1, len(word2)+1):
            for  c in range(1, len(word1)+1):
                if word1[c-1] == word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
        
        # print(dp)
        return dp[-1][-1]
                    