#https://leetcode.com/problems/count-asterisks/description/

class Solution:
    def countAsterisks(self, s: str) -> int:
        c = 0
        check = True
        for i in s:
            if i == '|':
                check = not check
            elif i == '*':
                if check:
                    c+=1
        return c
