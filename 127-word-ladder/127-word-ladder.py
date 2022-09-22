from collections import defaultdict

class Solution:
    def differByOne(self, word1, word2):        
        diffCount = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diffCount += 1
        return diffCount < 2
            
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord == beginWord:
            return 0
        
        if endWord not in wordList:
            return 0
        
        buckets = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                sh = word[:i] + "*" + word[i+1:]
                buckets[sh].append(word)
                
        # print(buckets)
        
        q = [[beginWord]]
        seen = set()
        pathLenght = 1
        
        while q:
            pathLenght += 1
            curr = q.pop()
            next_level = []
            neibors = []
            
            for word in curr:
                # print(curr)
                for i in range(len(word)):
                    sh = word[:i] + "*" + word[i+1:]
                    neibors.extend(buckets[sh])
            
            for nei in neibors:
                if nei == endWord:
                    return pathLenght
                
                if nei not in seen:
                    seen.add(nei)
                    next_level.append(nei)
                
            if next_level:
                q.insert(0, next_level)
        
        return 0
            
            
                    
        
                
#         if endWord == beginWord:
#             return 0
        
#         if endWord not in wordList:
#             return 0
        
#         seen = set()
#         q = [[beginWord]]
#         ans = 0
        
#         while q:
#             level = q.pop(0)
#             ans += 1
#             next_level = []
#             for curr in level:
#                 if curr == endWord:
#                     return ans
                
#                 seen.add(curr)
#                 for word in wordList:
#                     if self.differByOne(curr, word) and word not in seen:
#                         seen.add(word)
#                         next_level.append(word)
                        
#             if len(next_level) == 0:
#                 return 0
            
#             q.append(next_level)
                
    
                