class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def longPali(i,j):
            
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i-=1
                j+=1
                
            return s[i+1:j]
        
        maxLen = 0
        res = ''
        for i in range(len(s)):
            x = longPali(i,i)
            if len(x)>maxLen:
                maxLen = len(x)
                res = x
                
            x = longPali(i,i+1)
            if len(x)>maxLen:
                maxLen = len(x)
                res = x
                
        return res
        