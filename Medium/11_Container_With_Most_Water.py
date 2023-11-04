# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        left = 0
        right = size - 1
        quantity = 0

        while(left<right):
            new_area = min(height[left], height[right])*(right - left)
            quantity = max(quantity, new_area)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        
        return quantity
        