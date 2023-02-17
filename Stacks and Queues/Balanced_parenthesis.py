def isValid(left,right) :
    if left == '[' and right == ']' :
        return 1
    elif left == '{' and right == '}' :
        return 1
    elif left == '(' and right == ')' :
        return 1
    return 0

def isValidParenthesis(expression):
    stk = [] 
    for x in expression :
        if x in '{([' :
            stk.append(x) 
        else :
            if len(stk) == 0 :
                return 0 
            if isValid(stk[-1],x) :
                stk.pop() 
            else :
                return 0
    if len(stk) == 0 :
        return 1
    return 0




# Main Code

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)

    if ans:
        print("Balanced")
        
    else:
        print("Not Balanced")