def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(1,l):
            if( s.count(s[0:i]) * i == l ):
                return True
        return False
