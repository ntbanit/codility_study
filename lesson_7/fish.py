# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/
def solution(A, B):
    stack = [] # store downstream fishes alive
    count = 0 # count upstream fishes alive
    N = len(A)

    for i in range(N) :
        if B[i] == 1 : # downstream
            stack.append(A[i])
        else :
            # the larger upstream fish eat smaller downstream fishes it meet
            while stack and stack[-1] < A[i] : 
                stack.pop()
        
        # the upstream fish not meet anyone
        # or it eat all every downstream fishes 
        if B[i] == 0 and not stack :
            count += 1
    
    return count + len(stack)