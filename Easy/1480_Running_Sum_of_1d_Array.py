# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        x = 0
        for i in range(len(nums)):
            x += nums[i]
            ans.append(x)

        return ans