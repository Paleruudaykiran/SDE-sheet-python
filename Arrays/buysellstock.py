def maximumProfit(prices):
    mini = prices[0] 
    profit = 0 
    for i in range(1,len(prices)) : 
        cost = prices[i] - mini 
        mini = min(mini,prices[i]) 
        profit = max(profit,cost) 
    return profit

print(maximumProfit([1,2,0,3]))