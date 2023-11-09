# 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while(i<len(nums)):
            count = 0
            for j in range(len(nums)):
                if(nums[i] > nums[j]):
                    count+=1
                continue
            i+=1
            ans.append(count)

        return ans