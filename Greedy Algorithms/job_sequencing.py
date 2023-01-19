def jobScheduling(jobs):
    jobs = sorted(jobs,key = lambda x : x[1],reverse = True) 
    maxi = 0
    for i in range(len(jobs)) :
        maxi = max(maxi,jobs[i][0]) 
    lis = [-1 for i in range(maxi)] 
    ans = 0
    for t,p in jobs :
        if lis[t-1] == -1 :
            lis[t-1] = 1
            ans += p
        else :
            t -= 1
            while t != 0 :
                if lis[t-1] == -1 :
                    lis[t-1] = 1
                    ans += p
                    break
                t -= 1
    return ans
                