def restoreString(self, s: str, indices: List[int]) -> str:
        l = len(s)
        a = [0 for i in range(l)]
        
        for i in range(l):
            a[ indices[i] ] = s[i]
        
        return ''.join(a)
