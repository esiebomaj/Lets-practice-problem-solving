class Solution:
    def reverse(self, x: int) -> int:
        signed = x < 0
        x = abs(x)
        y = 0
        while x:
            print(x)
            y += (x%10)*(10**(len(str(x))-1))
            x = x//10
        # print(y)
        
        # y = y % ((2**31)-1)
        # print(y % ((2**31)-1))
        # print(((2**32)))
        if y >  (2**31):
            return 0
        
        return y if not signed else -y