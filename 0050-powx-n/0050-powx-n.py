class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
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
        