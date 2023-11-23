# 1464. Maximum Product of Two Elements in an Array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi1 = max(nums)
        nums.remove(maxi1)
        maxi2 = max(nums)

        return (maxi1 - 1)*(maxi2 - 1)