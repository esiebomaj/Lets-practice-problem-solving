class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = {i:[] for i in range(numCourses)}
        edgeCounts = {i:0 for i in range(numCourses)}
        
        for child, parent in prerequisites:
            adj[parent].append(child)
            edgeCounts[child] += 1
        
        sources = []
        
        for vertex in edgeCounts:
            if edgeCounts[vertex] == 0:
                sources.append(vertex)
                
                
        while sources:
            vertex = sources.pop()
            res.append(vertex)
            
            for child in adj[vertex]:
                print(child)
                edgeCounts[child] -= 1
                if edgeCounts[child] == 0:
                    sources.insert(0, child)
                    
                    
        if len(res) == numCourses:
            return res
        else:
            return []
        