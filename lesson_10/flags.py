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
    if M == 0 :
        return 0
    
    K = min(M, int(math.sqrt(N)) + 1)
    while K > 1 :
        count = 1
        lastFlag = peaks[0]
        for peak in peaks[1: ]:
            if peak - lastFlag >= K:
                count += 1
                lastFlag = peak
        # print(f"K={K} count={count}")
        if count >= K:
            return K
        K -= 1
    
    return 1