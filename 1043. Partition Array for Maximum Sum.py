# Partition Array of maximum sum

def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dic = [-1 for i in range(900)]
        def getMax(arr,k,v):
            if(dic[v]!=-1):
                return dic[v]
            if(len(arr[v:])==k):
                dic[v] = max(arr[v:])*k
                return dic[v]  
            else:
                m = 0
                for i in range(v,v+k):
                    t = len(arr[v:i+1])
                    if(t==0):
                        continue
                    p = max(arr[v:i+1])*t + getMax(arr[:],k,i+1)
                    m = max(m,p)
                dic[v] = m
                return m
        return getMax(arr,k,0)
