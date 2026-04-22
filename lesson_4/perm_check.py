# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
from collections import Counter
def solution(A):
    N, sum_arr = len(A), sum(A)
    counter = Counter(A)
    if sum_arr != (N + 1) * N // 2 :
        return 0
    for number in range(1, N + 1):
        if counter[number] != 1:
            return 0
    return 1