class Solution:
    def hammingWeight(self, n: int) -> int:
        # First method 
        # convert to binary and manually count the bits
#         b = ""
        
#         while n:
#             b = str(n%2) + b
#             n = n//2
            
#         count = 0
        
#         for i in b:
#             if i == "1":
#                 count += 1
                
#         return count
    
        # Second method
        count = 0
        while n:
            count += n%2
            n = n >> 1
        return count
        