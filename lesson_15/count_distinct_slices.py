# https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/
def solution(M, A):
    N = len(A)
    seen = set() 
    left = 0
    count = 0
    for right in range(N) :
        while A[right] in seen :
            seen.remove(A[left])
            left += 1
        seen.add(A[right])
        count += right - left + 1
        if count > 10**9 :
            return 10**9
    return count 