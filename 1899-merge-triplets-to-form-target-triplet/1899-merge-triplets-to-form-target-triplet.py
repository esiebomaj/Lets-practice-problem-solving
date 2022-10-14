class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cantUse = set()
        good = set()
        
        for i,n in enumerate(target):
            for j,t in enumerate(triplets):
                if t[i] > n:
                    cantUse.add(j)
                    
        if len(cantUse) >= len(triplets):
            return False
        
        for i,n in enumerate(target):
            for j,t in enumerate(triplets):
                if t[i] == n and j not in cantUse:
                    good.add(i)
                    
        return len(good) == 3 
        