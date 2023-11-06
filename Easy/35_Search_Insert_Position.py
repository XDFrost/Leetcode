# 35. Search Insert Position


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start+end)//2

        if target not in nums:
            if target>nums[len(nums) - 1]:
                return len(nums)

            for i in range(len(nums)):
                if target<nums[i]:
                    return i
                continue          

        if(target<=nums[mid]):
            for i in range(mid+1):
                if(target == nums[i]):
                    return i
                continue
            
        else:
            for i in range(mid+1, len(nums) - 1):
                if(target == nums[i]):
                    return i
                continue
        
        return len(nums) - 1
