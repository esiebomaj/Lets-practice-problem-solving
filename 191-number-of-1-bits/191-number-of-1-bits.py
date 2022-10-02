class Solution:
    def hammingWeight(self, n: int) -> int:
        b = ""
        while n:
            b = str(n%2) + b
            n = n//2
            
        count = 0
        
        for i in b:
            if i == "1":
                count += 1
                
        return count
        