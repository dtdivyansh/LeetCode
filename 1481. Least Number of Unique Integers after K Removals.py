def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        for i in arr:
            if(i in dic.keys()):
                dic[i]+=1
            else:
                dic[i]=1
        
        ans = [i for i in dic.values() ]
        ans.sort()
        print(ans)
        c=0
        while(k):
            if(k>=ans[c]):
                k-=ans[c]
                c+=1
            else:
                break
        return len(ans)-c
