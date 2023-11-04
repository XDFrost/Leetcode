# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        size = len(nums1)
        nums1.sort()
        
        if(size%2 != 0):
            return nums1[size//2]
        else:
            return mean([nums1[size//2 - 1],nums1[size//2]])
