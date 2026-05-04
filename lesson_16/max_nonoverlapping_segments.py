# https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments
def solution(A, B):
    if not A :
        return 0
    
    count = 1
    last = B[0] # always pick first segment (earliest end)
    for i in range(1, len(A)):
        if A[i] > last : # strictly not overlap
            count += 1
            last = B[i]
    return count 