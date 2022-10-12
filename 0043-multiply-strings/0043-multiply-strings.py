class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        2 non-negative intergers
        represented as strings
        """
        res = []
        
        for j,n in enumerate(reversed(num2)):
            carry = 0
            for i, m in enumerate(reversed(num1)):
                x = (int(n)*int(m)) + carry
                carry, x = x//10, x%10
                if i == 0:
                    res.append(x*(10**j))
                else:
                    res[-1] = res[-1] + ((10**(i+j))*x)
                    
            if carry > 0:
                res[-1] = res[-1] + ((10**(i+j+1))*carry)
                
            
        print(res)
        return str(sum(res))     