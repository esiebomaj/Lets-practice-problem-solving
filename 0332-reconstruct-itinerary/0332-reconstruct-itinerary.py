from collections import deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        
        adj = {s:deque() for s,d in tickets}
        
        for src, dest in tickets:
            adj[src].append(dest)
        
        print(adj)
            
        res = ["JFK"]
            
        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            
            if src not in adj or not adj[src]:
                return False
            
            tmp = adj[src].copy()
            for i,dest in enumerate(tmp):
                res.append(dest)
                adj[src].popleft()
                
                if dfs(dest):
                    return True
                
                res.pop()
                adj[src].append(dest)
            return False
                
        dfs("JFK")
        return res
          
                
            