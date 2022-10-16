from collections import deque
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1,n+1)}
        res = 0
        
        for edge in times:
            adj[edge[0]].append((edge[1], edge[2]))
        print(adj)
        seen = set()
        q = [(0, k)]
        heapq.heapify(q)
        
        while q:
            t, node = heapq.heappop(q)
            if node not in seen:
                seen.add(node)
                res = max(res, t)
                for childN, childT in adj[node]:
                    heapq.heappush(q, (t+childT, childN))
        
        print(seen, n)
        if len(seen) < n:
            return -1
        else:
            return res
                
            
        
        