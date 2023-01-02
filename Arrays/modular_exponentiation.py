def modularExponentiation(x, n, m):
    ans = 1
    while n > 0:
        if n % 2 == 0: 
            x = (x * x)%m
            n = n//2
        else :
            ans = (ans*x)%m 
            n -= 1 
    return ans

print(modularExponentiation(5,2,10))
# 5 ^ 2 = 25 => 25 % 10 = 5