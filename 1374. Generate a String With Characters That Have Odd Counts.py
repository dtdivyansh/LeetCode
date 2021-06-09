def generateTheString(self, n: int) -> str:
        if(n&1):
            #return ''.join('a' for i in range(n))
            return 'a'*n
        else:
            #return ''.join('a' for i in range(n-1))+'b'
            return 'a'*(n-1)+'b'
