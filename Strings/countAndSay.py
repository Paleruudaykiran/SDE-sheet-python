def writeAsYouSpeak(n):
    # Write your code here.
    if n == 1 :
        return 1 
    if n == 2 :
        return '11'
    s = "11"
    for i in range(3,n+1):
        ct = 1
        s = s + '$' 
        curr = ""
        for j in range(1,len(s)) :
            if s[j] != s[j-1] :
                curr = curr + str(ct) + s[j-1]
                ct = 1 
            else :
                ct += 1
        s = curr
    return s