#https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/
import math
def solution(A):
    N = len(A)
    if N <= 2: # can not find any peak
        return 0

    peaks = set() 
    for i in range(1, N - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.add(i)
    if not peaks :
        return 0 

    max_k = N // 2 + 1
    # print(max_k)
    for K in range(2, max_k + 1) :
        # print(f"K={K} ")
        if N % K != 0 :
            continue
        blocks = N // K
        peak_count = 0
        curr = 0
        while curr < N :
            old_peak_count = peak_count
            for i in range(curr, curr + K):
                # print(f"blocks={blocks} K={K} curr={curr} i={i} peak_count={peak_count}")
                if i in peaks :
                    # print(f"i={i} in peaks")
                    peak_count += 1
                    break
            if old_peak_count == peak_count : # all block has to have a peak 
                break 
            curr += K 
        # print(f"blocks={blocks} K={K} peak_count={peak_count}")
        if peak_count == blocks :
            return blocks

    return 1
