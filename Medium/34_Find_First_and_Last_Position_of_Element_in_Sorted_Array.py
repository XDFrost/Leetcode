# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        if target in nums:
            for i in range(0,n):
                if nums[left]==nums[right]:
                    return [left,right] 
                elif nums[left]<target:
                    left+=1
                else:
                    right-=1
        else:
            return [-1,-1]                           