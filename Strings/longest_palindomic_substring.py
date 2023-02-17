def longestPalinSubstring(s):
    maxi,ans = 1,s[0]
    for i in range(len(s)) :
        for j in range(len(s)) :
            if s[i:j+1] == s[i:j+1][::-1] :
                if j-i+1 > maxi :
                    maxi = j-i+1 
                    ans = s[i:j+1] 
    return ans