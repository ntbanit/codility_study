# https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/
def solution(S):
    stack = 0 # only need store the length of stack is enough
    for ch in S :
        if ch == '(':
            stack += 1
        else :
            # should have at least 1 open before close bracket
            if stack == 0: 
                return 0 
            
            stack -= 1
    
    return 1 if stack == 0 else 0