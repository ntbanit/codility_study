def coins(n: int) -> int:
    """
    Returns the number of coins showing tails after n people flip coins.
    
    Key insight: A coin ends tails iff it has an ODD number of divisors.
    Only perfect squares have an odd number of divisors (the square root
    is the only unpaired divisor). So the answer = floor(sqrt(n)).
    
    floor(sqrt(n)) is computed in O(log n) via binary search.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0

    lo, hi = 0, min(n, 10**9)  # cap hi since sqrt(n) <= n

    while lo < hi:
        mid = (lo + hi + 1) // 2  # upper-mid to avoid infinite loop
        if mid * mid <= n:
            lo = mid
        else:
            hi = mid - 1

    return lo  # lo == floor(sqrt(n)) == number of perfect squares in [1..n]