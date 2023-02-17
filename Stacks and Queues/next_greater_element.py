def nextGreater(arr,n):
    NGE = [-1]*n 
    stk = []
    for i in range(n) :
        if len(stk) == 0 :
            stk.append(i) 
        else :
            while len(stk) != 0 and arr[stk[-1]] < arr[i] :
                NGE[stk.pop()] = arr[i] 
            stk.append(i) 
    while len(stk) != 0 :
        NGE[stk.pop()] = -1
    return NGE