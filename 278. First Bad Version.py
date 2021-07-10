def firstBadVersion(self, n):
        mini = 2**31
        i,j = 1,n
        while(i<=j):
            mid = (i+j)//2
            res = isBadVersion(mid)
            
            if(res):
                mini = min(mid,mini)
                j = mid-1
            else:
                i = mid+1
                
        return mini
