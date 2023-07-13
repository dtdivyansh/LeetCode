#https://leetcode.com/problems/decode-the-message/description/

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        table = {}
        j = 0
        for i in key:
            if i == ' ':
                continue
            if i not in table:
                table[i] = alpha[j]
                j+=1
            if j == 26:
                break
        
        decode = ''
        for i in message:
            decode+= table[i] if i != ' ' else ' '
        
        return decode
