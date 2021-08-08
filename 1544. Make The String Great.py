def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for i in s[1:]:
            #print(stack,i)
            if(stack and i.isupper() and i.lower()==stack[-1]):
                stack.pop()
            elif(stack and i.islower() and i.upper()==stack[-1]):
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
