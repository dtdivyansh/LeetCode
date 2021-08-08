def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if(i=='../'):
                if(stack):
                    stack.pop()
            elif(i=='./'):
                pass
            else:
                stack.append(1)
        return len(stack)
