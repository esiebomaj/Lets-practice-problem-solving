class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        using union find
        """
        par = [i for i in range(len(edges)+1)]
        rank = [i for i in range(len(edges)+1)]
        
        def find(x):
            p = par[x]
            while p != par[p]:
                p = par[p]
                
            return p
        
        def union(v1, v2):
            p1,p2 = find(v1), find(v2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                
            else:
                par[p1] = p2
                rank[p2] += p1
                
            return True
        
        for x,y in edges:
            if not union(x,y):
                return [x,y]
            
        
#         adj = {i:[] for i in range(1,len(edges)+1)}
        
#         for x,y in edges:
#             adj[x].append(y)
#             adj[y].append(x)
        
#         cantRemove =  set()
        
#         for i in adj:
#             if len(adj[i]) == 1:
#                 cantRemove.add(i)
        
#         for x,y in edges[::-1]:
#             if x not in cantRemove and y not in cantRemove:
#                 return [x,y]
            
        