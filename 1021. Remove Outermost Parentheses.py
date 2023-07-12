#https://leetcode.com/problems/remove-outermost-parentheses/

def removeOuterParentheses(self, s: str) -> str:
        stack = ''
        ans = ""
        a = 0
        b = 0
        for i in s:
            stack+=i
            if(i=='('):
                a+=1
            else:
                b+=1
            if(a==b):
                ans+=stack[1:-1]
                a,b=0,0
                stack = ''
        return ans
