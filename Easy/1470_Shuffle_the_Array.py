# 1470. Shuffle the Array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        i = 0
        while(n<len(nums)):
            ans.append(nums[i])
            ans.append(nums[n])
            i+=1
            n+=1
            
        return ans