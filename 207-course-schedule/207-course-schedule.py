from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Using topological sort
        # this question is basically a cyle deection problem 
        # we know that for a cyclic graph, it is not posible to find a complete topological sort
        
        # we can leverae this to detect the cycle
        
        res = []
        
        adj = { i:[] for i in range(numCourses) }
        eCounts = { i:0 for i in range(numCourses) }
        
        for child, parent in prerequisites:
            adj[parent].append(child)
            eCounts[child] += 1
            
        sources = []
        
        for i in eCounts:
            if eCounts[i] == 0:
                sources.append(i)
                
        while sources:
            vertex = sources.pop()
            res.append(vertex)
            for child in adj[vertex]:
                eCounts[child] -= 1
                
                if eCounts[child] == 0:
                    sources.insert(0, child)
                    
        return len(res) == numCourses
            
            
            
            