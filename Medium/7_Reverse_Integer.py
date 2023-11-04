# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if x<INT_MIN or x>INT_MAX:
            return 0

        flag = False
        if x>0:
            flag = False
        elif x<0:
            flag = True
        else:
            return 0
        
        if flag == True:
            x = abs(x)

        reverse = 0
        while(x>0):
            num = x%10
            reverse = reverse*10 + num
            x = x//10    
        
        if reverse < INT_MIN or reverse > INT_MAX:
            return 0
        
        if(flag == True):
            reverse = -1 * reverse
            return reverse
        else:
            return reverse
