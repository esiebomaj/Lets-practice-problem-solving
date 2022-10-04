class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Optimized solution
        # TIme: O(N) space: O(1)
        
        digits = digits[::-1]
        carry = 0
        
        for i in range(len(digits)):
            digit = digits[i]
            
            if i == 0:
                digit = digit + 1
                
            digit = digit + carry
            
            carry, newDigit = digit//10, digit%10
            
            digits[i] = newDigit
            
        if carry:
            digits.append(carry)
        
        return digits[::-1]
    
                
        # Time O(N), space: O(N)
        res = []
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            digit = digits[i]
            
            if i == len(digits)-1:
                digit = digit + 1
            
            digit = digit + carry
            carry, digit = digit//10, digit%10
            
            res.append(digit)
            
            
        if carry:
            res.append(carry)
            
        return res[::-1]
        