# 16. 3Sum Closest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        nums.sort()
        ans = 'inf'
        min_dis = 'inf'
        for i in range(size-2):
            j = i+1
            k = size - 1
            while(j<k):
                check = nums[i] + nums[j] + nums[k]
                dis = abs(target - check)
                if(dis<min_dis):
                    min_dis = dis
                    ans = check
                if(check<target):
                    j+=1
                elif(check>target):
                    k-=1
                else:
                    return ans
        
        return ans