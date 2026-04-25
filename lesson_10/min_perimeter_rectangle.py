# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/

def solution(N):
    answer = (1 + N) * 2
    i = 2
    while i * i <= N:
        if N % i == 0 : 
            perimeter = (i + N // i) * 2
            answer = min(answer, perimeter)
        i += 1
    return answer