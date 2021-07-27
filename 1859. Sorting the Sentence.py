def sortSentence(self, s: str) -> str:
        s = s.split()
        l = len(s)
        ans = [0 for i in range(l)]
        
        for w in s:
            ans[ int(w[-1])-1 ] = w[:-1]
            
        return ' '.join(ans)
