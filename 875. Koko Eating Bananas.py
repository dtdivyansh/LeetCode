import math
def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = math.ceil(sum(piles)/h)
        maxi = max(piles)
        res = 10**9+1
        while(mini<=maxi):
            mid = (mini+maxi)//2
            val = sum([math.ceil(i/mid) for i in piles])   
            if(val<=h):
                res = min(res,mid)
                maxi = mid-1
            else:
                mini = mid+1
                
        return res
