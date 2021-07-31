import heapq as hq
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        c=0
        n=len(piles)
        piles.sort(reverse=True)
        i,j=1,n-1
        while(i<j):
            c+=piles[i]
            i+=2
            j-=1
            
        return c
