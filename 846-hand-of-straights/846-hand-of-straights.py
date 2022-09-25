from collections import Counter
import heapq

class Solution:
    def decrement(self, key, dic):
        # special methodto decrement value in a dictionary
        # if the value reaches 0, we remvoe it fron the dictionary
        dic[key] -= 1
        if dic[key] == 0:
            del dic[key]
            
            
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        print(counter)
        
        heapq.heapify(hand)
        while hand:
            curr = heapq.heappop(hand)
            print(curr)
            if curr not in counter:
                continue
                
            j = curr
            count = 1
            
            self.decrement(j, counter)
            
            while j+1 in counter and count < groupSize:
                
                j += 1
                print(j, count)

                self.decrement(j, counter)
                count += 1
                    
            if count < groupSize:
                return False
            
       
                
        return True
        
                        
     
                    
            