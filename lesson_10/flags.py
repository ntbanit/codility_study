# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/
import math
def solution(A):
    peaks = []
    N = len(A)
    for i in range(1, N - 1) : 
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)

    # print(peaks)

    M = len(peaks)
    K = min(M, int(math.sqrt(N)))
    max_flags = 1 
    while K > 1 :
        count = 1
        lastFlag = peaks[0]
        for peak in peaks[1: ]:
            if peak - lastFlag >= K:
                count += 1
                lastFlag = peak
        # print(f"K={K} count={count}")
        max_flags = max(max_flags, min(K, count))
        K -= 1
    return max_flags
