# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
def solution(N, A):
    output = [0] * N
    cur_max = max_counter = 0
    for op in A :
        if op == N + 1:
            max_counter = cur_max
            continue 
        
        i = op - 1
        if output[i] < max_counter :
            output[i] = max_counter
        output[i] += 1
        cur_max = max(cur_max, output[i])
    
    for i in range(N):
        if output[i] < max_counter :
            output[i] = max_counter
    
    return output