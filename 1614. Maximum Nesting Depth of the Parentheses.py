def maxDepth(self, s: str) -> int:
        stack = []
        top = 0
        m = 0
        for i in s:
            if i == '(':
                stack.append(i)
                top+=1
                if(top>m):
                    m = top
            elif i == ')':
                stack.pop()
                top-=1
        return m
