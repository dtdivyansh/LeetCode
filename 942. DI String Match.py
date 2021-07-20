def diStringMatch(self, s: str) -> List[int]:
        i,j = 0,len(s)
        ans = []
        for k in s:
            if(k=='I'):
                ans.append(i)
                i+=1
            else:
                ans.append(j)
                j-=1
        while(i<=j):
            ans.append(i)
            i+=1
            
        return ans
