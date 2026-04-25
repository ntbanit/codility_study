# https://codility.com/media/train/7-MaxSlice.pdf
def quadratic_max_slice(A):
    max_sum = A[0]
    for i in range(len(A)):
        current_sum = 0
        for j in range(i, len(A)):
            current_sum += A[j]
            max_sum = max(max_sum, current_sum)
    return max_sum

def golden_max_slice(A):
    max_ending = max_slice = A[0]
    for i in range(1, len(A)):
        max_ending = max(A[i], max_ending + A[i])
        max_slice = max(max_slice, max_ending)
    return max_slice

A = [3, 2, -6, 4, 0, 5, -7, 3, 5, -2, 4, -1]
print(quadratic_max_slice(A))
print(golden_max_slice(A))