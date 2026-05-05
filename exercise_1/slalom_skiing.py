# https://app.codility.com/programmers/trainings/1/slalom_skiing/
# COPIED SOLUTION 100% 
def solution(A):
    n = len(A)
    if n == 0:
        return 0

    # Coordinate compress
    rank = {v: i + 1 for i, v in enumerate(sorted(A))}
    m = n # all distinct

    class BIT:
        def __init__(self, size):
            self.size = size
            self.tree = [0] * (size + 1)

        def update(self, i, val):
            while i <= self.size:
                self.tree[i] = max(self.tree[i], val)
                i += i & (-i)
        
        def query(self, i): # prefix max [1..i]
            res = 0
            while i > 0:
                res = max(res, self.tree[i])
                i -= i & (-i)
            return res

    # bit0: phase 0 → prefix max (A[j] < A[i])
    # bit01: phases 0+1 → suffix max (A[j] > A[i]) via reversed rank
    # bit12: phases 1+2 → prefix max (A[j] < A[i])
    bit0 = BIT(m)
    bit01 = BIT(m)
    bit12 = BIT(m)

    ans = 0
    for i in range(n):
        r = rank[A[i]]
        r_rev = m + 1 - r # reversed rank for suffix queries

        p0 = 1 + bit0.query(r - 1)
        p1 = 1 + bit01.query(r_rev - 1) # A[j] > A[i] → r_rev_j < r_rev
        p2 = 1 + bit12.query(r - 1)

        bit0.update(r, p0)
        bit01.update(r_rev, max(p0, p1)) # future j may transition FROM phase 0 or 1
        bit12.update(r, max(p1, p2)) # future j may transition FROM phase 1 or 2

        ans = max(ans, p0, p1, p2)

    return ans