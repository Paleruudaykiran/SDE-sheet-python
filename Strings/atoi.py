def atoi(s):
    n = 0
    for ch in s:
        if ch >= '0' and ch <= '9' :
            n = n*10 + ord(ch)-ord('0') 
    if s[0] == '-' :
        return -n
    return n