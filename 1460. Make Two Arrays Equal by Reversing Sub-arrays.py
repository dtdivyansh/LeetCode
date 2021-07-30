def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
            if(target[i]!=arr[i]):
                if(target[i] in arr[i+1:]):
                    j = arr[i:].index(target[i])
                    j = j+i
                    v = i
                    while(v<j):
                        arr[v],arr[j] = arr[j],arr[v]
                        v+=1
                        j-=1
                        
                else:
                    return False
        return True
