def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def fun(s,i,j):
            nonlocal ans
            if(i==j):
                ans.append(''.join(s))
                return
            if(s[i].isdigit()):
                fun(s,i+1,j)
            else:
                s1 = s.copy()
                s1[i] = s1[i].upper()
                fun(s1,i+1,j)
                
                s2 = s.copy()
                s2[i] = s2[i].lower()
                fun(s2,i+1,j)
                
                return
            
        s = [i for i in s]
        j = len(s)
        fun(s,0,j)
        return ans
