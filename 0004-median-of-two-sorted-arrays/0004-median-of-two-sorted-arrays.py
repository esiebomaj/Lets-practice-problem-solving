class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N = len(nums1) + len(nums2)
        half = N//2 
        
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l = 0
        r = len(nums1)-1
        
        while True:
            mid1 = (l+r)//2
            mid2 = half - mid1 - 2
            
            max1 = nums1[mid1] if mid1 >= 0 else float(-inf)
            min1 = nums1[mid1+1] if mid1+1 < len(nums1) else float(inf)
            
            max2 = nums2[mid2] if mid2 >= 0 else float(-inf)
            min2 = nums2[mid2+1] if mid2+1 < len(nums2) else float(inf)
            
            
            if max1 <= min2 and max2 <= min1:
                if N%2:
                    # ODD
                    return min(min1, min2)
                else:
                    # EVEN
                    print(max1, max2, min1, min2, max(max1, max2) + min(min1, min2))
                    return (max(max1, max2) + min(min1, min2))/2
                 
            elif max1 > min2:
                r = mid1-1
            else:
                l = mid1+1
                
       
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums1.extend(nums2)
        
#         nums1.sort()  # -  #NLogN
        
#         if len(nums1)%2 != 0:
#             return nums1[int((len(nums1)/2))]
#         else:
#             return (nums1[int((len(nums1)/2)-1)] + nums1[int(len(nums1)/2)])/2
        
    
        
        