# https://app.codility.com/programmers/lessons/12-euclidean_algorithm/common_prime_divisors/
import math 

def solution(A, B):
    def remove_factor(n, g) :
        while True : 
            d = math.gcd(n, g)
            if d == 1 :
                return n
            while n % d == 0 :
                n //= d

    cnt = 0
    for N, M in zip(A, B) :
        if N == M :
            cnt += 1
            continue 

        gc = math.gcd(N, M) 
        if gc == 1 :
            continue 

        if remove_factor(N, gc) == 1 and remove_factor(M, gc) == 1:
            cnt += 1

    return cnt 