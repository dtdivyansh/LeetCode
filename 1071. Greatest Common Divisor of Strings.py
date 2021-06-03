def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ''
        ans = ''
        n1 = len(str1)
        n2 = len(str2)
        for i in str1:
            res+=i
            n3 = len(res)
            if( res*(n1//n3) == str1 and res*(n2//n3)==str2 ):
                ans=res
        return ans
