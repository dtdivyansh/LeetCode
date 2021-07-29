def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        c=0
        for i in s:
            if(i == '('):
                stack.append(i)
                c+=1
            else:
                if(stack):
                    if(stack[-1]=='('):
                        stack.pop()
                        c-=1
                    else:
                        stack.append(i)
                        c+=1
                             
                else:
                    stack.append(i)
                    c+=1
        return c
