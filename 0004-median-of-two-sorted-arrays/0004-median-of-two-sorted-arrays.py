class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        
        nums1.sort()  # -  #NLogN
        
        if len(nums1)%2 != 0:
            return nums1[int((len(nums1)/2))]
        else:
            return (nums1[int((len(nums1)/2)-1)] + nums1[int(len(nums1)/2)])/2
        
    
        
        