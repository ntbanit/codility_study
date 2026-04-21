#https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
def solution(A):
    answer = 1001 * 100000
    arr_sum = sum(A)
    prefix = 0
    for i in range(0, len(A) - 1) :
        prefix += A[i]
        gap = prefix - (arr_sum - prefix)
        answer = min(answer, abs(gap))
    return answer 
