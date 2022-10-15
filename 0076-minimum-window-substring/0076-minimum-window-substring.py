class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,0
        res = ''
        resLen = float(inf)
        
        tWindow = {}
        sWindow = {}
        
        for i in t:
            if i in tWindow:
                tWindow[i] += 1
            else:
                tWindow[i] = 1
                sWindow[i] = 0
                
        goodCount = len(tWindow)
        
        while r < len(s) or goodCount == 0:
            if goodCount == 0:
                if r-l < resLen:
                    res = s[l:r]
                    resLen = r-l
                    
                # reduce the window size by moving l
                if s[l] in tWindow:
                    char = s[l]
                    sWindow[char] -= 1
                    if sWindow[char] == tWindow[char]-1:
                        goodCount += 1
                    
                l += 1
            else:
                # increase the window size by moving r 
                if s[r] in tWindow:
                    char = s[r]
                    sWindow[char] += 1
                    if sWindow[char] == tWindow[char]:
                        goodCount -= 1
                r += 1
                
        return res