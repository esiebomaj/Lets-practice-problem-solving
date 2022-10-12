class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        dic = {}
        for i in t:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
        l,r = 0,0
        count = len(dic)
        resCount = float(inf)
        res = ''
        while r < len(s) :
            
            if count == 0:
                if r-l < resCount:
                    res = s[l:r]
                    resCount = len(res)
                    

                # move l
                if s[l] in dic:
                    former = dic[s[l]]
                    dic[s[l]] += 1
                    curr = dic[s[l]]

                    if former <= 0 and curr > 0:
                        count += 1
                    if curr <= 0 and former > 0:
                        count -= 1
                
                l += 1
                
            else:
                # move r
                if s[r] in dic:
                    former = dic[s[r]]
                    dic[s[r]] -= 1
                    curr = dic[s[r]]

                    if former <= 0 and curr > 0:
                        count += 1
                    if curr <= 0 and former > 0:
                        count -= 1
                        
                r += 1
                
        if count == 0:    
            if r-l < resCount:
                res = s[l:r]
                resCount = len(res)
                
        while l <= (len(s)-len(t)) and count == 0:
            if count == 0:
                if r-l < resCount:
                    res = s[l:r]
                    resCount = len(res)
            
                # move l
            if s[l] in dic:
                former = dic[s[l]]
                dic[s[l]] += 1
                curr = dic[s[l]]

                if former <= 0 and curr > 0:
                    count += 1
                if curr <= 0 and former > 0:
                    count -= 1
                
                
            l += 1
                
            
        return res
            