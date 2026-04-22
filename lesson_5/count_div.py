# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
def solution(A, B, K):
    i_min = (A + K - 1) // K # ceiling
    i_max = B // K # floor
    # print(f"i_min={i_min} i_max={i_max}")
    return i_max - i_min + 1
