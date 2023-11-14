# 1684. Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        check = set(allowed)

        for i in words:
            flag = True
            for j in i:
                if j not in check:
                    flag = False
                continue
            
            if flag == True:
                count+=1
        
        return count
        