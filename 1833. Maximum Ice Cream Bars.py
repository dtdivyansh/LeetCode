def maxIceCream(self, costs: List[int], coins: int) -> int:
        s = sum(costs)
        l = len(costs)
        if(s<=coins):
            return l
        costs.sort()
        while(s>coins):
            l-=1
            s-=costs[l]
        
        return l
