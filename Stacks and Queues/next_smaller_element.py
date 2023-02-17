def nextSmallerElement(arr,n):
    stk = [] 
    ans = [-1]*n
    for i in range(n) :
        if len(stk) == 0 :
            stk.append(i) 
        else :
            while len(stk) != 0 and arr[i] < arr[stk[-1]] :
                ans[stk.pop()] = arr[i]
            stk.append(i) 
    return ans