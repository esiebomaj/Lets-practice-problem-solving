class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        y = 0
        i = len(str(x))-1
        while x:
            y += (x%10)*(10**i)
            x = x//10
            i -= 1


        if y > (2**31):
            return 0
        
        return y if not negative else -y