# https://codility.com/media/train/6-Leader.pdf
def goldenLeader(A):
    size = 0
    value = None

    for i in range(len(A)):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if A[i] != value:
                size -= 1
            else:
                size += 1

    candidate = -1
    if size > 0:
        candidate = value

    count = 0
    for i in range(len(A)):
        if A[i] == candidate:
            count += 1

    if count > len(A) // 2:
        return candidate

    return -1