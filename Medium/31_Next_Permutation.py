# 31. Next Permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = -1
        for i in range(len(nums) - 2, -1, -1):
            if(nums[i]<nums[i+1]):
                ind = i
                break
            
        if(ind == -1):
            nums.reverse()
            return nums
            
        for i in range(len(nums) - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        left = ind+1
        right = len(nums) - 1
        while(left<right):
            if(nums[left]>nums[right]):
                nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

        return nums

