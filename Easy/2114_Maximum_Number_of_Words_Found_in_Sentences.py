# 2114. Maximum Number of Words Found in Sentences]

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        max_len = 1   

        if len(sentences) > 1:
            for sen in sentences:
                if sen == "" or sen == " ":
                    continue
                else:
                    count = sen.count(" ")
                    if count+1 > max_len:
                        max_len = count+1
                    continue
            
            return max_len

        elif len(sentences) == 1:
            if sentences[0] == "" or sentences[0] == " ":
                return max_len - 1
            else:
                count = sentences[0].count(" ")
                return count+1


        else:
            return max_len - 1
