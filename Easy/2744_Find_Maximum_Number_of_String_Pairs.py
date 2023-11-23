# 2744. Find Maximum Number of String Pairs

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        i = 0

        while(len(words)>1):
            flag = False    
            for j in range(len(words)):
                if(words[i] == words[j]): continue
                if(words[i] == words[j][::-1]):
                    count+=1
                    words.remove(words[j])
                    words.remove(words[i])
                    flag = True
                    break
            if flag == False:
                words.remove(words[i])
        
        return count
        