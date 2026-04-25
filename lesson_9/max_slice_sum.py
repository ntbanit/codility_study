# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/
def solution(A):
    max_slice = max_curr = A[0]
    for number in A[1:]:
        max_curr = max(max_curr + number, number)
        max_slice = max(max_slice, max_curr)

    return max_slice