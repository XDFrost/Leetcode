# 1913. Maximum Product Difference Between Two Pairs

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return []
        
        maxi = max(nums)
        nums.remove(maxi)
        maxi2 = max(nums)

        mini = min(nums)
        nums.remove(mini)
        mini2 = min(nums)

        return (maxi * maxi2) - (mini * mini2)
        