def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while(columnNumber):
            columnNumber-=1
            res = chr(65 + columnNumber%26) + res
            columnNumber //= 26
        return res
