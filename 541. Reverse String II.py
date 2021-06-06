def reverseStr(self, s: str, k: int) -> str:
        l = 2*k
        i = 0
        final = ""
        while(i < len(s)):
            v = (l+i)//2
            res = s[v-1:i:-1]
            res+=s[i]
            final = final+res+s[v:l]
            i = l
            l = l + 2*k
        return final
