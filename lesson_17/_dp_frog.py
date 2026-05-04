def frog(S, k, q):
    n = len(S)
    dp = [1] + [0] * k
    for j in range(1, k + 1):
        for i in range(n):
            if S[i] <= j:
                dp[j] = (dp[j] + dp[j- S[i]]) % q
    return dp[k]