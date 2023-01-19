def findMinimumCoins(amount):
    i = len(denominations) - 1
    ans = 0
    while i >= 0 and amount != 0 :
        if denominations[i] <= amount :
            ans = ans + amount//denominations[i] 
            amount = amount % denominations[i] 
        i -= 1
    return ans