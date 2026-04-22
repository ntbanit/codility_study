# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
def solution(A):
    # with each number 1, count how many number 0 before it
    N = len(A)
    prefix_zero = [0] * (N + 1)
    count = 0
    for i in range(N) :
        prefix_zero[i + 1] = prefix_zero[i]
        if A[i] == 0:
            prefix_zero[i + 1] += 1
        else :
            count += prefix_zero[i]
            if count > 10**9:
                return -1

    return count