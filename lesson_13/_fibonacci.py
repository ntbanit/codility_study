# https://codility.com/media/train/11-Fibonacci.pdf
def solution(A, m):
    # Step 1: Generate all Fibonacci numbers up to m (~31 of them)
    fibs = []
    a, b = 1, 1
    while a <= m:
        fibs.append(a)
        a, b = b, a + b
    print(fibs)
    # Step 2: Mark all values <= m that are sums of two Fibonacci numbers
    # O(31^2) = O(1) — constant work regardless of input size
    can_be_sum = [False] * (m + 1)
    for i in range(len(fibs)):
        for j in range(i, len(fibs)):        # j >= i to avoid duplicate pairs
            s = fibs[i] + fibs[j]
            if s <= m:
                can_be_sum[s] = True
            else:
                break                         # fibs is sorted, no need to go further

    # Step 3: Answer each query in O(1)
    return [can_be_sum[x] for x in A]


# --- Test ---
m = 1_000_000
A = [3, 10, 12, 100, 1000000]
print(solution(A, m))