# https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/
import math

def solution(N, M):
    lcm = N * M // math.gcd(N, M) 
    return lcm // M