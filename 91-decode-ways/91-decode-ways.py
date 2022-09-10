class Solution:
    def numDecodings(self, s: str) -> int:
        # if its start from 0 return false 
        if s[0] == "0":
            return 0
        
        dp = [1]*len(s)
        
        for i in range(1, len(s)):
            if int(s[i]) == 0:
                if 1 <= int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-2]
                else:
                    return 0
            else:
                if int(s[i-1]) == 0:
                    dp[i] = dp[i-1]
                elif 1 <= int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-2] + dp[i-1]
                else:
                    dp[i] = dp[i-1]
        print(dp)
        return dp[-1]
    
        # for each nunmber 
            # if the num is 0 =>  it can only form 2 letters with the previous on
                # if prev num is 2 or 1:
                    # take the prev prev  forward 
                # else                   
                    # return 0 

            
            # else 
                # if the prev i 
                # if prev is btw 10 and 26
                    # we add prev and prev prev ones 
                # else 
                    # take prev
        
            
                
            
            
            