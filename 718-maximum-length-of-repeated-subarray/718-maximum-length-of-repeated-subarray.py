class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # if there are unique values
        # then we can solve ths problem using a hashmap as so
#         hashmap = {}
#         res = 0
#         for i in range(len(nums1)):
#             hashmap[nums1[i]] = i
        
#         i = 0
#         while i < len(nums2):
#             num = nums2[i]
#             if num in hashmap:
#                 j = i
#                 k = hashmap[num]
#                 currLongest = 0
#                 while j < len(nums2) and k < len(nums1) and nums2[j] == nums1[k]:
#                     currLongest += 1
#                     j += 1
#                     k += 1
#                 res = max(currLongest, res)
#                 i = j-1
                
#             i += 1
#         return res
                
        
        dp = [[0 for i in range(len(nums1)+1)] for k in range(len(nums2)+1)]
        res = 0
        
        for i in range(1, len(nums2)+1):
            for j in range(1, len(nums1)+1):
                if nums1[j-1] == nums2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    
                else:
                    dp[i][j] = 0
                    
                res = max(res, dp[i][j])
        return res
                