class Solution:
    def reverseBits(self, n: int) -> int:
        
        # convert to binary
        b = str(bin(n))[2:]
        b = "0"*(32-len(b)) + b
        
        # reverse
        b = b[::-1]
        
        # convert back to decimal
        res = 0
        pos = len(b)-1
        for i in b:
            res += (int(i)*(2**pos))
            pos -= 1
                    
        return res
        