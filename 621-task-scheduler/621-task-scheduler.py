from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [[-counter[i], i] for i in counter]
        heapq.heapify(heap)
        
        res = 0
        
        while heap:
            k = n
            stack = []
            while k >= 0:
                if heap:
                    curr = heapq.heappop(heap)
                    curr[0] += 1
                    if curr[0] < 0:
                        stack.append(curr)
                        
                    res += 1
                    
                elif (not heap) and (len(stack)>0):
                    res += 1
                    
                k -= 1
                    
            while stack:
                curr = stack.pop()
                heapq.heappush(heap, curr)
                    
        # print(res)
        return res
                    
            
        