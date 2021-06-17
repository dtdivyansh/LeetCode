def getWinner(self, arr: List[int], k: int) -> int:
        c = 0
        mx = arr[0]
        for i in range(1,len(arr)):
            if(arr[i]>mx):
                c=0
                mx = arr[i]
            c+=1
            if(c==k):
                return mx
        return mx
