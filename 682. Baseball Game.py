def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if(i[-1].isnumeric()):
                #print(i)
                stack.append(int(i))
                
            elif(i=='+'):
                stack.append(stack[-1]+stack[-2])
            
            elif(i=='D'):
                stack.append(2*stack[-1])
                
            else:
                stack.pop()
        
        return sum(stack)
