def mushroom_pick_m2(A, K, M):
    output = 0
    N = len(A)
    for P in range(M) :
        curr = 0
        # go right
        for i in range(P + 1) :
            if K + i >= N :
                break
            curr += A[K + i]
        # go left
        for i in range(1, M - P - 1) :
            if K - i < 0 :
                break
            curr += A[K - i]
        # print(f"P={P} curr={curr}")
        output = max(output, curr)
        
    return output

def mushroom_pick_nm(A, K, M):
    output = 0
    N = len(A)
    # prefix index from 1 to N 
    prefix = [0] * (N + 1)
    for i in range(N) :
        prefix[i + 1] = prefix[i] + A[i]

    for P in range(M) :
        # go right from K to K + P
        right = min(N - 1, K + P)
        curr = prefix[right + 1] - prefix[K]
        # go left from K - 1 to K - (M - P - 2)
        left = max(0, K - (M - P - 2))
        curr += prefix[K] - prefix[left]
        # print(f"P={P} curr={curr}")
        output = max(output, curr)
    
    return output

"""
zero-indexed array A of n (1 ≤ n ≤ 100000) integers a₀, a₁, …, aₙ₋₁
(0 ≤ aᵢ ≤ 1000)
itegers k and m (0 ≤ k, m < n)
"""
A = [2, 3, 7, 5, 1, 3, 9]
K = 4
M = 6
# expected 25
print(mushroom_pick_m2(A, K, M))
# expected 25
print(mushroom_pick_nm(A, K, M))

# below is sample code from pdf file 
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k- 1] + A[k- 1]
    return P

def count_total(P, x, y):
    return P[y + 1]- P[x]

def mushrooms(A, k, m):
    result = 0
    n = len(A)
    pref = prefix_sums(A)
    for p in range(min(m, k) + 1):
        left_pos = k- p
        right_pos = min(n- 1, max(k, k + m- 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k- (m- 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))
    return result
print(mushrooms(A, K, M))