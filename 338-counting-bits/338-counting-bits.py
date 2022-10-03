class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        offset = 1
        
        for i in range(1, n+1):
            offset = i if i == offset*2 else offset
            dp[i] = 1 + dp[i-offset]
            
        return dp
    
        result = []
        for i in range(0,n+1): # NlogN
            result.append(self.toBinary(i).count('1'))

        return result
    
    def toBinary(self, num): # Log(n)
        if num == 0:
            return '0'
        
        remainders = ''
        while  num > 0:
            re = num%2
            remainders = str(re) + remainders
            num = num//2
            
        return remainders