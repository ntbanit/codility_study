# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
def solution(A):
    N = len(A)
    min_slice = 100001
    start = -1
    for i in range(N - 1): 
        slice_two = (A[i] + A[i + 1]) / 2
        if min_slice > slice_two:
            start = i
            min_slice = slice_two
        if i < N - 2: 
            slice_three = (A[i] + A[i + 1] + A[i + 2]) / 3
            if min_slice > slice_three:
                start = i
                min_slice = slice_three
    return start