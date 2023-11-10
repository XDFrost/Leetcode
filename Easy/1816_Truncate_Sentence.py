# 1816. Truncate Sentence

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        spaces = s.count(" ")
        ans = ""
        if(spaces<k):
            return s
        else:
            words = s.split()
            for i in range(k):
                ans+=words[i]
                if(i+1 == k):
                    continue
                else: ans+=" "
            
            return ans
        