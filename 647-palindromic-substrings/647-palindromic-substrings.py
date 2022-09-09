class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def paliCount(i,j):
            count = 0
            while i >=0 and j < len(s) and s[i] == s[j] :
                count+=1
                i-=1
                j+=1
            return count
        
        for i in range(len(s)):
            res += paliCount(i,i)
            res += paliCount(i,i+1)
        
        return res
            
        
        