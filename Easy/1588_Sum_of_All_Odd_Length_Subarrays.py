# 1588. Sum of All Odd Length Subarrays

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        odd_sum = 0
        n = len(arr)
        
        for i in range(n):
            for j in range(i+1, n+1):
                if (j-i)%2:
                    odd_sum += sum(arr[i:j])

        return odd_sum
