# https://app.codility.com/programmers/lessons/17-dynamic_programming/number_solitaire/
def solution(A):
    MIN_VALUE = -10**9
    N = len(A)
    dp = [MIN_VALUE] * N
    dp[0] = A[0]
    for i in range(N):
        for j in range(1, 7):
            if i - j < 0 :
                break
            dp[i] = max(dp[i], dp[i - j] + A[i])
    return dp[N - 1]