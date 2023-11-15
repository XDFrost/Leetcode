# 2656. Maximum Sum With Exactly K Elements

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        ans = 0
        for i in range(k):
            ans+=maximum+i

        return ans
        