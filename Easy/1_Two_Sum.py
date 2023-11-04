# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            sec_num = target - nums[i]
            for j in range(i+1, size):
                if nums[j] == sec_num:
                    return [i,j]
                    break
                continue