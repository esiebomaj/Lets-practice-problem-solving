from collections import Counter

class Solution:
    def decrement(self, key, dic):
        dic[key] -= 1
        if dic[key] == 0:
            del dic[key]
        
    def increment(self, key, dic):
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
        
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        counter1 = Counter(s)
        counter2 = {}
        
        similar = 0
        start = 0
        
        for i, char in enumerate(s):
            print(i, char)
            # increment counter2
            self.increment(char, counter2)
            
            # decrement counter1
            self.decrement(char, counter1)
        
            if counter2[char] == 1:
            # we just added it to counter 2
                similar += 1

            if char not in counter1:
                # we just removed it from counter 1
                similar -= 1

            if similar == 0:
                res.append(s[start:i+1])
                counter2 = {}
                start = i+1
                
        print(res)
        return [len(i) for i in res]
        
        
        """
        res = []
        counter1 - all chars
        counter2 - curr window
        we want to find the first substring from the begining where counter 1 and counter2 has no similar key
        similar = 0
        for i in s:
        # increment counter2
        # decrement counter1
        
        if i in counter1 and counter2[i] == 1:
        # we just added it to counter 2
        similar += 1
        
        if i not in counter1:
        similar -= 1
        
        if similar == 0:
        res.append(s[:i])
        counter2 = {}
            
        
        EXAMPLE
        "ababcbacadef egdehijhklij"
        similar = 2
        counter1 = {
a:0
b:0
c:0
        e:2
        f:0
        g:1
        h:2
        i:2
        j:2
        d:1
        k:1
        l:1
        }
        
        {
        d:1
        e:1
        f:1
        }
        
        
        
        counter2 = {
        a:4
        b:3
        c:2
        }
        
        
        """
      
        