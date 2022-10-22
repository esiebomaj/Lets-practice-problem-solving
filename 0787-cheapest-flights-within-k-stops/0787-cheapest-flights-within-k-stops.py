from queue import PriorityQueue
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Bellman Fords algorithm
        
        """
        
        prices = [float(inf)]*n
        prices[src] = 0
        
        for i in range(k+1):
            temp = prices.copy()
            for fro, to, cost in flights:
                price = prices[fro] + cost
                temp[to] = min(price, temp[to])
                
            prices = temp
            
        return -1 if prices[dst] == float(inf) else prices[dst]
        
            
                
            
        