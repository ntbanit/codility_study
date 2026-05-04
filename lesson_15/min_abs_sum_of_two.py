# https://app.codility.com/programmers/lessons/15-caterpillar_method/min_abs_sum_of_two/start/
# https://app.codility.com/programmers/lessons/15-caterpillar_method/min_abs_sum_of_two/start/
def solution(A):
    N = len(A)
    if N == 1:
        return abs(2 * A[0])
    
    A.sort()
    # print(A)
    MAX_NUM = 2 * 10**9
    left, right = 0, N - 1
    answer = MAX_NUM
    while left <= right :
        curr = abs(A[left] + A[right])
        answer = min(answer, curr)
        # print(f"left={left} right={right} curr={curr}")
        leftMove = MAX_NUM
        if left + 1 <= right :
            leftMove = abs(A[right] + A[left + 1])
        rightMove = MAX_NUM
        if right - 1 >= left :
            rightMove = abs(A[right - 1] + A[left])

        if leftMove * rightMove == 0 :
            return 0

        if leftMove < rightMove :
            left += 1
        elif leftMove > rightMove :
            right -= 1
        else :
            break 
        
    return answer 