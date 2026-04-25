# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/
########### COPIED CODE ############
def solution(A):
    N = len(A)
    left = [0] * N # best subarray sum ending at i
    right = [0] * N # best subarray sum starting at i
    for i in range(1, N - 1) : # have exclude 0 to have valid X 
        left[i] = max(left[i - 1] + A[i], 0) # exclude the number if negative
    for i in range(N - 2, 0, -1): 
        right[i] = max(right[i + 1] + A[i], 0)
    
    max_sum = 0
    for Y in range(1, N - 1):
        max_sum = max(max_sum, left[Y - 1] + right[Y + 1])
    return max_sum