# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/
def solution(N):
    if N == 1 :
        return 1
    cnt = 2 
    i = 2
    while (i * i) <= N :
        if N % i == 0 :
            cnt += 2 
        i += 1
    i -= 1
    if i * i == N :
        cnt -= 1
    return cnt 