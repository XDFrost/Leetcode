# 1313. Decompress Run-Length Encoded List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)//2):
            freq = nums[2*i]
            val = nums[2*i + 1]

            for x in range(0, freq):
                ans.append(val)
        
        return ans