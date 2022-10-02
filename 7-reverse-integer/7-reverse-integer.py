class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        res = 0
        i = len(str(x))-1
        
        while x:
            res += (x%10)*(10**i)
            x = x//10
            i -= 1


        if res > (2**31):
            return 0
        
        return res if not negative else -res