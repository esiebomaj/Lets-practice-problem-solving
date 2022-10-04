class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
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
    
    # [1,2,9]
                

        