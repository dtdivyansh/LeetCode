def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        return ' '.join( [ s[i] for i in range(k) ] )
