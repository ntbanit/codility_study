# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit
def solution(A):
    if not A :
        return 0
    max_profit = 0
    hold = A[0]
    for price in A[1:]: 
        if price < hold :
            hold = price
        else :
            max_profit = max(max_profit, price - hold)
    return max_profit