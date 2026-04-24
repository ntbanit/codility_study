# https://app.codility.com/programmers/lessons/8-leader/dominator
from collections import Counter

def solution(A):
    counter = Counter(A)
    N = len(A)
    dom = N // 2
    for i in range(N):
        if counter[A[i]] > dom :
            return i
    return -1