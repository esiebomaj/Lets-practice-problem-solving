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
    
#     gas = [1,2,3,4,5] 
#     cost =[3,4,5,1,2]
#     cum =[-2,-2,-2,3,3]
    
#     gas = [2,3,4], 
#     cost = [3,4,3]
#     cum  = [-1,-1,1]
    
#     gas = [2,4,1,3]
#     cost = [1,3,2,2]
#     cum = [1,1,-1,1]
            
            
        