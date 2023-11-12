# 2535. Difference Between Element Sum and Digit Sum of an Array

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit = []
        for i in nums:
            if i>=10:
                while(i>0):
                    rem = i%10
                    digit.append(rem)
                    i = i//10
            else:
                digit.append(i)
            

        return abs(sum(nums) - sum(digit))
