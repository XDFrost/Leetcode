# 15. 3Sum

class Solution:
    def threeSum(self, nums):
        output = []
        nums.sort()
        size = len(nums)

        for i in range(size - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            low = i + 1
            high = size - 1
            target = 0 - nums[i]

            while low < high:
                if nums[low] + nums[high] == target:
                    out = [nums[i], nums[low], nums[high]]
                    if out not in output:
                        output.append(out)
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < target:
                    low += 1
                else:
                    high -= 1

        return output
