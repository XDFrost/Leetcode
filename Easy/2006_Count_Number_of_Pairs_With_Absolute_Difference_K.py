# 2006. Count Number of Pairs With Absolute Difference K

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # count = 0
        # start = 0
        # check = 0
        # while(start<len(nums)):
        #     if(start<check):
        #         if abs(nums[start] - nums[check]) == k:
        #             count+=1
        #         check+=1
        #     else: check+=1
        #     if(check == len(nums)):
        #         start+=1
        #         check = 0

        # return count


        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(i<j):
        #             if abs(nums[i] - nums[j]) == k:
        #                 count+=1
        #             j+=1
        #         else:
        #             j+=1
        
        # return count


        nums_dict, count = {}, 0
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        for num in nums:
            if num + k in nums_dict:
                count += nums_dict[num + k]
        return count
        