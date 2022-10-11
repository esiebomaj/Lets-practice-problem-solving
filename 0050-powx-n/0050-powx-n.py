class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = x
        negPow = n < 0
       
        n = abs(n)
        
        j = 1
        
        # n = 10
        # j = 8, res = 16*16
        
        while j*2 <= n:
            res = res * res
            j = j * 2
            
        
        for i in range(j, n):
            res = res*x
        
        return 1/res if negPow else res
        