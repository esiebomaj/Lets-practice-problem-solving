class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cum = []
        for i in range(len(gas)):
            cum.append(gas[i]-cost[i])
            
        if sum(cum) < 0:
            return -1
        
        maxSum = float(-inf)
        maxSumId = None
        currSum = 0
        
        for i in range(len(gas)-1, -1, -1):
            currSum = currSum + cum[i]
            if currSum > maxSum:
                maxSum = currSum
                maxSumId = i
        return maxSumId
        
            
#         for i in range(len(gas)):
#             start = True
#             availableGas = 0
#             j = i
            
#             while availableGas >= 0:  
#                 if j == i and not start: 
#                     return i
#                 start = False
#                 availableGas += gas[j]
#                 availableGas -= cost[j]
#                 j = (j + 1)%len(gas)
                
                
#         return -1