# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
def solution(A):
    N = len(A) + 1 
    return N * (N + 1) //2 - sum(A)