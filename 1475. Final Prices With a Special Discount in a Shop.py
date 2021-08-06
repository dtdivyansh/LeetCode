def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        l = len(prices)
        for i in range(l-1):
            j = i+1
            stack = []
            
            while(j<l and prices[i]<prices[j]):
                j+=1
                  
            if(j!=l):
                stack.append(j)
                prices[i]-=prices[stack[-1]]
            #print(i,j,prices,stack)  
            
        return prices
