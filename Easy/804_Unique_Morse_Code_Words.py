# 804. Unique Morse Code Words

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        # ans = []
        # for i in words:
        #     sign = ""
        #     for j in range(len(i)):
        #         sign+=code[ord(i[j]) - 97]
        #     ans.append(sign)
            
        
        # ans = set(ans)
        # return len(ans)


        ans = set()
        c = 0
        for i in words:
            sign = ""
            for j in range(len(i)):
                sign+=code[ord(i[j]) - 97]
            if sign not in ans:
                ans.add(sign)
                c+=1
        
        return c
