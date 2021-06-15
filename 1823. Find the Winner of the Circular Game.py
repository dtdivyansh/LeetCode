def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]
        k-=1
        i=0
        while(len(arr)>1):
            i = (i+k)%len(arr)
            arr.pop(i)
        return arr[0]
