# 1662. Check If Two String Arrays are Equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        comp1 = "".join(word1)
        comp2 = "".join(word2)

        return comp1 == comp2