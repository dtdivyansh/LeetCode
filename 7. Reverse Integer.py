#https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        val = [i for i in str(x)]
        i = 0 if x >= 0 else 1 
        j = len(val) - 1
        while(i<j):
            val[i], val[j] = val[j], val[i]
            i+=1
            j-=1
        ans = int(''.join(val))
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        return ans

#Faster approach

class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
            x1=0-x
            s=str(x1)
        else:
            s=str(x)
        temp=""
        for i in s:
            temp=i+temp
        if(int(temp)>=2**31 or int(temp)<-2**31):
            return 0
        if(x<0):
            return 0-int(temp)
        return int(temp)
