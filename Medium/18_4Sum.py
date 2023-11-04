# 18. 4Sum

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        size = len(nums)
        output = []
    
        for i in range(size - 3):
            for j in range(i+1, size - 2):
                start = j+1
                end = size - 1
                while end>start:
                    check = sum([nums[i] + nums[start] + nums[end] + nums[j]])
                    if(check == target):
                        out = [nums[start], nums[end], nums[j], nums[i]]
                        if out not in output:
                            output.append(out)
                        start+=1
                        end-=1
                    elif(check>target):
                        end-=1
                    else:
                        start+=1
    
        return output
                              