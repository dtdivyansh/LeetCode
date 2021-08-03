def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]
        a,b=1,1
        while(b<k):
            fib.insert(0,a+b)
            b = a+b
            a = b-a
        
        s,c=0,0
        i=0
        while(s!=k):
            if(s+fib[i]<=k):
                s+=fib[i]
                c+=1
            i+=1
        
        return c
