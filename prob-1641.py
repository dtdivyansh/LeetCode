# COUNT SORTED VOWEL STRINGS

def countVowelStrings(self, n: int) -> int:
        s = 'aeiou'
        dic = {(s,1):5}
        def find(s,n):
            if((s,n) in dic.keys()):
                return dic[(s,n)]
            if(n==1):
                dic[(s,n)] = len(s)
                return dic[(s,n)]
            else:
                t = 0 
                for i in range(len(s)):
                    t += find(s[i:],n-1)
                dic[(s,n)] = t
                return dic[(s,n)]
        return find(s,n)
