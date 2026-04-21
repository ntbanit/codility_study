# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
def solution(N):
    longest = 0
    index = 0
    previous = -1
    while N > 0 :
        bit = N % 2
        if bit == 1 :
            if previous != -1 :
                longest = max(longest, index - previous - 1)
            previous = index
        index += 1
        N //= 2
    return longest 