class Solution:
    def countBits(self, n: int) -> List[int]:
        
        """
        # O(N) solution 
        We want to try to get a repeating pattern in the counts of 1
        
        Let use 10
        0 = 0
        1 = 1
        2 = 10
        3 = 11
        
        4 = 100
        5 = 101
        6 = 110
        7 = 111
        
        8 =  1000
        9 =  1001
        10 = 1010
        11 = 1011
        12 = 1100
        13 = 1101
        14 = 1110
        15 = 1111
        
        16 = 10000
        17 = 10001
        18 = 10010
        19 = 10011
        20 = 10100
        
        We can see that there is a pattern 
        at [2,4,8,16,32... etc] the sequence repeats from 0 with an addition of an extra 1 most significant bit
        i.e @ 4 the sequence starts from 0 with an aditional 1 as the MSB
        
        4 => 1 00
        5 => 1 01
        6 => 1 10
        7 => 1 11
        
        The pattern start again at 8
        repeating sequence from 0 with a extra 1 in the MSB
        
        8 =>  1 000
        9 =>  1 001
        10 => 1 010
        11 => 1 011
        12 => 1 100
        13 => 1 101
        14 => 1 110
        15 => 1 111
        
        So we can conclude that 
        dp[i] = 1 + dp[i-offset]
        where offset is [2,4,8,16, etc]
        so at any of this points we have to adjust our offset 
        this makes it posible to start from 0 at any of these point
        """
        dp = [0]*(n+1)
        offset = 1
        
        for i in range(1, n+1):
            offset = i if i == offset*2 else offset
            dp[i] = 1 + dp[i-offset]
            
        return dp
    
    
        """
        Time: O(nlogn)
        More intuitive 
        for each value in the range we can calculate its bin and manually cout the 1's
        """
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