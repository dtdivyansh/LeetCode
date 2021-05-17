def lenLongestFibSubseq(self, arr: List[int]) -> int:
        S = set(arr)
        n = len(arr)
        mx = 0
        for i in range(n):
            for j in range(i+1,n):
                x = arr[j]
                y = arr[j] + arr[i] 
                
                l = 2
                
                while(y in S):
                    z = x+y
                    x = y
                    y = z
                    l+=1
                    if(l>mx):
                        mx=l
                        
        return mx if mx>=3 else 0
