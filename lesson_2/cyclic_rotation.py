# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
def solution(A, K):
    N = len(A)
    result = [0] * N
    for i in range(N):
        result[(i + K) % N] = A[i]
    return result 