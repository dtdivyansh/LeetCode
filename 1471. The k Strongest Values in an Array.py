def getStrongest(self, arr: List[int], k: int) -> List[int]:
        ans = []
        arr.sort()
        n = len(arr)
        med = arr[(n-1)//2]
        i=0
        j=n-1
        while(len(ans)!=k):
            if(i>j):
                break
            else:
                if(abs(arr[i]-med)>abs(arr[j]-med)):
                    ans.append(arr[i])
                    i+=1
                elif(abs(arr[i]-med)<abs(arr[j]-med)):
                    ans.append(arr[j])
                    j-=1
                else:
                    if(arr[i]>arr[j]):
                        ans.append(arr[i])
                        i+=1
                    else:
                        ans.append(arr[j])
                        j-=1
        return ans
