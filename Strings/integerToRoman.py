def intToRoman(n):
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    vals = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    i = len(roman)-1
    ans = ""
    while n > 0 :
        if n >= vals[i] :
            ct = n//vals[i] 
            ans = ans + roman[i]*ct
            n = n - ct*(vals[i])
        i -= 1 
    return ans 
print(intToRoman(55))


