def minDeletions(self, s: str) -> int:
        dic  = {}
        l=0
        for i in s:
            if(i in dic.keys()):
                dic[i]+=1
            else:
                dic[i]=1
                l+=1
        
        arr = list(dic.values())
        arr.sort()
        c = 0
        
        for i in range(l-2,-1,-1):
            if(arr[i+1]==0):
                s = sum(arr[0:i+1])
                c+=s
                break
            elif(arr[i]==arr[i+1]):
                arr[i]-=1
                c+=1
            elif(arr[i]>arr[i+1]):
                c = c + arr[i]-arr[i+1]+1
                arr[i] = arr[i+1]-1
        
        return c
