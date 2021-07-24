def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        else:
            stack = []
            while(x>0):
                a = x%10
                stack.append(a)
                x = x//10
            i,j = 0,len(stack)-1
            while(i<j):
                if(stack[i]!=stack[j]):
                    return False
                i+=1
                j-=1
            return True
