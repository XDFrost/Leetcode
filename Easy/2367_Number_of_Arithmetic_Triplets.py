# 2367. Number of Arithmetic Triplets

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        # for i in range(len(nums)-2):
        #     j = i+1
        #     k = j+1
        #     while(k<len(nums)):
        #         if j<len(nums):
        #             if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
        #                 count+=1
        #                 j+=1
        #                 k+=1
        #             elif nums[j] - nums[i] < diff: 
        #                 j+=1
        #             else:
        #                 k+=1
        #         else:
        #             break
        # return count
        

        for num in nums:
            if num+diff in nums and num+diff+diff in nums:
                count+=1
            
        return count