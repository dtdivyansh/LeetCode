def tribonacci(self, n: int) -> int:
        if(n==0):
            return 0
        if(n==1 or n==2):
            return 1
        arr = [-1 for i in range(n+1)]
        arr[1],arr[2],arr[0] = 1,1,0
        def fun(n):
            nonlocal arr
            if(arr[n]!=-1):
                return arr[n]
            else:
                arr[n] = fun(n-1) + fun(n-2) + fun(n-3)
                return arr[n]
        
        return fun(n)
