def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        res = perm.copy()
        c=0
        while(True):
            arr = [0 for i in range(n)]
            for i in range(len(perm)):
                arr[i] = perm[n//2+(i-1)//2] if i&1 else perm[i//2]    
            c+=1
            perm = arr
            if(perm==res):
                break
        return c
