# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
def solution(A):
    A.sort()
    output = A[-1] * A[-2] * A[-3] # 3 largest of array
    output = max(output, A[-1] * A[0] * A[1]) # 2 smallest (negative ) and 1 largest
    if len(A) >= 4 :
        output = max(output, A[-4] * A[-2] * A[-3]) # ??? 
    return output 