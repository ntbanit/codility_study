# https://app.codility.com/programmers/lessons/15-caterpillar_method/abs_distinct/
def solution(A):
    seen = set()
    for number in A :
        number = -number if number < 0 else number 
        seen.add(number)
    return len(seen)