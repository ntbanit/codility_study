# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
def solution(X, A):
    seen = set() 
    pos_sum = 0 
    for time in range(len(A)) :
        if A[time] not in seen :
            seen.add(A[time])
            pos_sum += A[time]
            if pos_sum == X * (X + 1) // 2:
                return time 
    return -1
