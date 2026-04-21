#https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
def solution(A):
    if len(A) == 1:
        return A[0]
    result = A[0]
    for num in A[1 : ]: 
        result ^= num 
    return result 