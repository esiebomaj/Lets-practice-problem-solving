from collections import Counter
import heapq

class Solution:
    def decrement(self, key, dic):
        # special method to decrement value in a dictionary
        # if the value reaches 0, we remvoe it fron the dictionary
        dic[key] -= 1
        if dic[key] == 0:
            del dic[key]
            
            
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        
        heapq.heapify(hand)
        while hand:
            curr = heapq.heappop(hand)

            if curr not in counter:
                continue
                
            j = curr
            count = 1
            
            self.decrement(j, counter)
            
            while j+1 in counter and count < groupSize:
                
                j += 1

                self.decrement(j, counter)
                count += 1
                    
            if count < groupSize:
                return False
            
       
                
        return True
        
                        
     
                    
            