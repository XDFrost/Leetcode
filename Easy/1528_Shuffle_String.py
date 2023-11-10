# 1528. Shuffle String

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ""
        size = len(indices)
        i = 0
        j = 0
        while(i!=size):
            if(indices[j] == i):
                ans+=s[j]
                i+=1
                j = 0
            else:
                j+=1

        return ans
        