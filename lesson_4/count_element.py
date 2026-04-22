def slow_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)

    for i in range(n):
        for j in range(n):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change

            if sum_a == sum_b:
                return True

            sum_a -= change
            sum_b += change

    return False

def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] += 1
    return count

def fast_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)

    d = sum_b - sum_a
    if d % 2 == 1:
        return False

    d //= 2
    print(d)
    count = counting(A, m)
    print(count)
    for i in range(n):
        if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
            print(f"i={i}")
            return True

    return False

A = [1, 2, 3, 4]
B = [2, 4, 3, 5]
m = 5
print(slow_solution(A, B, m))
print(fast_solution(A, B, m))