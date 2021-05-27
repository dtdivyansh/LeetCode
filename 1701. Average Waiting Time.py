def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n= len(customers)
        curr= customers[0][0]+customers[0][1]
        tot=  curr-customers[0][0]
        customers.pop(0)
        for order in customers:
            if( curr>order[0] ):
                curr= curr + order[1]
                tot = tot + ( curr - order[0] )
            else:
                curr = order[0] + order[1]
                tot = tot + (curr - order[0])
        ans = tot/n
        
        return ans
