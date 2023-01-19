def maximumMeetings(start, end):
    meetings = [(st,ed) for st,ed in zip(start,end)] 
    d = {} 
    for i in range(len(meetings)) :
        d[(meetings[i])] = i+1
    meetings = sorted(meetings,key = lambda x : x[1])
    lis = []
    prev_end = -1 
    for i in range(len(meetings)) :
        if i == 0 :
            lis.append(d[meetings[i]])
            prev_end = meetings[i][1] 
        else :
            if prev_end < meetings[i][0] :
                lis.append(d[meetings[i]])
                prev_end = meetings[i][1] 
    return lis
               