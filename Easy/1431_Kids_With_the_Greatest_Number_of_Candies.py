# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans : bool = []
        maximum = max(candies)
        for i in range(len(candies)):
            if(candies[i] + extraCandies >= maximum):
                ans.append(True)
            else: ans.append(False)

        return ans
