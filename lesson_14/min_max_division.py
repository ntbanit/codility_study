# https://app.codility.com/programmers/lessons/14-binary_search_algorithm/min_max_division/
def solution(K, M, A):
    left, right = max(A), sum(A) 
    N = len(A)

    def check(candidate):
        count = 1
        cur_sum = 0
        for i in range(N):
            if cur_sum + A[i] <= candidate :
                cur_sum += A[i]
            else :
                cur_sum = A[i]
                count += 1
                if count > K:
                    return False
            # print(f"candidate={candidate} A[i]={A[i]} cur_sum={cur_sum} count={count}")
        return count <= K # if < K, it can be empty arrays

    while left <= right :
        mid = (left + right) // 2
        if check(mid) :
            right = mid - 1
        else :
            left = mid + 1
    return left 