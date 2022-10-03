class Solution:
    def hammingWeight(self, n: int) -> int:
        #### First method 
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
    
        #### Second method
        # we find out if the last number is 1 or 0 
        # We can do this by checking it its even or odd (n%2)
        # We know that odd numbers end with 1 while even numbers end with 0
        # then we do bitwise right shift operation on it to remove the last digit 
        # and continue exploring the remaining digits untill the number becomes 0
        # count = 0
        # while n:
        #     count += n%2
        #     n = n >> 1
        # return count
        
        
        #### Third method
#       we use a trick
#       We know that (n & (n-1)) will remove a 1 digit from the bin
#       e.g 4(100)
#       4 & (4-1) = 4 & (3) = 000
        
#         100
#       & 011
#         ---
#         000 (effectively removing a 1 digit from the bin)
#         ---
        
#        e.g 10 (1010)

#         10 & (10-1) = 10 & (9)
#         1010
#       & 1001
#         ----
#         1000 (again effectively removing a 1 bit from the bin of the number)
#         ----        

### SUMMARY 
#       We know that (a & (a-1)) will remove a single 1 digit from the binary of a 
#       we can keep doing this till a is zero and count the number of times 
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count
        