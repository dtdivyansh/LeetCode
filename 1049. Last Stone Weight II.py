def lastStoneWeightII(self, stones: List[int]) -> int:
        def minDiffSubset(arr,n,s):
            if(n<0 and s!=0):
                return False
            elif(s==0):
                return True
            elif(arr[n]<=s):
                return minDiffSubset(arr, n-1, s-arr[n]) or minDiffSubset(arr, n-1, s)
            else:
                return minDiffSubset(arr, n-1, s)
    
        def getMinDiff(arr,n,s):
            m = 10000007
            for i in range(s//2,-1,-1):
                if( minDiffSubset(arr, n-1,i )):
                    return s-2*i
                
        return getMinDiff(stones,len(stones),sum(stones))
