# BEST TIME TO BUY SELL STOCKS

def maxProfit(prices):
        if(not prices):
            return 0
        sell = [0]
        buy = [0]
        profit = [0]
        
        for i in range(len(prices)):
            if( (buy[-1] < i) and (prices[i] > prices[ buy[-1] ]) ):
                sell.append(i)
            if( (prices[i] < prices[ buy[-1] ]) ):
                buy.append(i)
            
            val = prices[ sell[-1] ] - prices[ buy[-1] ]
            if(val>profit[0] and buy[-1]<sell[-1]):
                profit[0] = val
                
        return profit[0]
