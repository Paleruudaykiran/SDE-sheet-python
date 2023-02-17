def sortStack(stack):
    if len(stack) == 0 :
        return 
    tp = stack.pop() 
    sortStack(stack) 
    insertCorrectPosition(stack,tp) 

    return stack

def insertCorrectPosition(stack,tp) :
    if len(stack) == 0 or tp > stack[-1] :
        stack.append(tp) 
        return 
    ele = stack.pop() 
    insertCorrectPosition(stack,tp) 
    stack.append(ele)
    