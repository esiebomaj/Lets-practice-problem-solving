
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Brute force solution
        """
        
        if x == 0:
            return 0
        if n == 0:
            return 1
        res = 1
        negPow = n < 0
        
        n = abs(n)
        
        for i in range(n):
            res = res*x
        
        return 1/res if negPow else res
    

    def myPow(self, x: float, n: int) -> float:
        """
        OPTIMIZED SOLUTION
        """
        return x**n
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = x
        negPow = n < 0
       
        n = abs(n)
        
        j = 1
        
        while j*2 <= n:
            res = res * res
            j = j * 2
            
        
        for i in range(j, n):
            res = res*x
        
        return 1/res if negPow else res
        