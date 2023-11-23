# 1534. Count Good Triplets

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(len(arr)) :
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and  abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans+=1
        
        return ans


        # ans = 0
        # for i in range(len(arr)) :
        #     start = i+1
        #     start_ = i+2
        #     end = len(arr) - 1
        #     while(start_ <= end):
        #         if abs(arr[i] - arr[start]) <= a and  abs(arr[start] - arr[start_]) <= b and abs(arr[i] - arr[start_]) <= c:
        #             ans+=1
        #         start_+=1
            
        
        # return ans
