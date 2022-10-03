class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0,n+1):
            # result.append(bin(i)[2:].count('1'))
            result.append(self.toBinary(i).count('1'))

        return result
    
    def toBinary(self, num):
        if num == 0:
            return '0'
        
        remainders = ''
        while  num > 0:
            re = num%2
            remainders = str(re) + remainders
            num = num//2
            
        return remainders
        