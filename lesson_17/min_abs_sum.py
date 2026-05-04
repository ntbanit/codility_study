# https://app.codility.com/programmers/lessons/17-dynamic_programming/min_abs_sum/start/
from collections import Counter 
def solution(A):
    A = [abs(num) for num in A]
    total = sum(A)
    target = total // 2

    dp = [-1] * (target + 1)
    dp[0] = 0
    count = Counter(A)
    for value in range(1, 101) :
        if value not in count :
            continue
        for j in range(0, target + 1) :
            if dp[j] >= 0 :
                dp[j] = count[value]
            elif j >= value and dp[j - value] > 0 :
                dp[j] = dp[j - value] - 1
    
    # for j in range(0, target + 1) :
    #     if dp[j] >= 0 :
    #         print(f"dp[{j}]={dp[j]}")

    for i in range(target, -1, -1):
        if dp[i] >= 0 :
            # print(f"i={i}")
            return total - 2 * i
    return total