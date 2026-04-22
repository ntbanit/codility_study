# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
def solution(A):
    seen = set(A)
    max_pos = max(A) + 1
    for num in range(1, max_pos + 1) :
        if num not in seen :
            return num 
    return 1