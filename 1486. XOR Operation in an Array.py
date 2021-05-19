def xorOperation(self, n: int, start: int) -> int:
     '''xor = start
        
        for i in range(1,n):
            xor = xor^( start + 2*i )
        return xor'''
        return functools.reduce(lambda a,b : a^b, (start+2*i for i in range(n)))
