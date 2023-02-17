def largestRectangle(arr):
    stk = [] 
    maxa = 0 
    n = len(arr) 
    for i in range(len(arr)+1) :
        while len(stk) != 0 and (i == n or arr[i] <= arr[stk[-1]]) :
            tpid = stk.pop() 
            if len(stk) == 0 :
                width = i
            else :
                width = i - stk[-1] - 1
            maxa = max(maxa,arr[tpid]*width) 
        stk.append(i) 
    return maxa