# https://app.codility.com/programmers/trainings/1/flood_depth/
def solution(A):
    N = len(A)
    maxLeft, maxRight = 0, 0
    left, right = 0, N - 1
    answer = 0
    while left < right : 

        if A[left] < A[right] :
            if A[left] < maxLeft :
                answer = max(answer, maxLeft - A[left])
            else :
                maxLeft = A[left]
            left += 1
        
        else :
            if A[right] < maxRight : 
                answer = max(answer, maxRight - A[right])
            else :
                maxRight = A[right]
            right -= 1
    
    return answer