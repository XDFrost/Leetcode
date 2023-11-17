# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = set(nums)   
        # ans = []

        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return 1

        # mini = min(nums) 
        # maxi = max(nums)

        # for i in range(mini, maxi):
        #     length = 1
        #     current = i
        #     while(current in nums and current+1 in nums):
        #         current = current+1
        #         length+=1
                
        #     ans.append(length)

        # return max(ans)



        nums = set(nums)   
        ans = 0

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num+length in nums:
                    length+=1
                ans = max(length, ans)

        return ans