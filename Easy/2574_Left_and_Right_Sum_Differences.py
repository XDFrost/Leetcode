# 2574. Left and Right Sum Differences


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftsum = [0] * n
        leftsum.append(0)
        for i in range(1, len(nums)):
            leftsum[i] = nums[i-1] + leftsum[i-1]
        
        rightsum = [0] * n
        total = sum(nums) - nums[0]
        rightsum[0] = total
        for i in range(1, len(nums)-1):
            rightsum[i] = rightsum[i-1] - nums[i]

        ans = [abs(leftsum[i] - rightsum[i]) for i in range(n)]

        return ans