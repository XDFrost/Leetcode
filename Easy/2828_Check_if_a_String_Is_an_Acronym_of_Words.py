# 2828. Check if a String Is an Acronym of Words

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        comp = "".join(i[0] for i in words)
        
        return s==comp

        # return "".join(i[0] for i in words) == s
        