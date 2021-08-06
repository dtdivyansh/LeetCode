def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        p = 'Push'
        o = 'Pop'
        i=0
        l = len(target)
        for j in range(1,n+1):
            if(j==target[i]):
                i+=1
                ans.append(p)
                if(i==l):
                    break
            else:
                ans.append(p)
                ans.append(o)
        return ans
