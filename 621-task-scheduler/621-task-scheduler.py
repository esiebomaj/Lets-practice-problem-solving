from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [[-counter[i], i] for i in counter]
        # print(heap)
        heapq.heapify(heap)
        # print(heap)
        res = ""
        while heap:
            print(heap)
            k = n
            stack = []
            while k >= 0:
                if heap:
                    curr = heapq.heappop(heap)
                    curr[0] += 1
                    if curr[0] < 0:
                        stack.append(curr)
                        
                    res += curr[1]
                    
                elif (not heap) and (len(stack)>0):
                    res += " "
                    
                k -= 1
                    
            while stack:
                curr = stack.pop()
                # curr[0] += 1
                # if curr[0] < 0:
                heapq.heappush(heap, curr)
                    
        print(res)
        print(len(res))
        return len(res)
                    
            
        