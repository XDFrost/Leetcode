#  1929. Concatenation of Array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        nums1 = nums
        ans.extend(nums1)
        ans.extend(nums)
        return ans