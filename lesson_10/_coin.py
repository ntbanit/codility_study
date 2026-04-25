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


# ── Verification ────────────────────────────────────────────────────────────

def coins_brute(n: int) -> int:
    """O(n log n) simulation for correctness checking."""
    coin = [0] * (n + 1)
    for i in range(1, n + 1):
        k = i
        while k <= n:
            coin[k] ^= 1   # flip (same as (coin[k] + 1) % 2 but faster)
            k += i
    return sum(coin[1:])


if __name__ == "__main__":
    import math
    import time

    print(f"{'n':>12} | {'O(logN)':>8} | {'Brute':>8} | {'Match':>6} | {'Time (µs)':>10}")
    print("-" * 55)

    test_cases = [1, 5, 10, 16, 100, 1_000, 10_000, 10**9, 10**18]

    for n in test_cases:
        t0 = time.perf_counter()
        fast = coins(n)
        elapsed = (time.perf_counter() - t0) * 1e6

        if n <= 10_000:
            brute = coins_brute(n)
            match = "✓" if fast == brute else "✗"
            # also double-check against math.isqrt
            assert fast == math.isqrt(n), f"Mismatch at n={n}"
        else:
            brute = "—"
            match = f"≡ isqrt" if fast == math.isqrt(n) else "✗"

        print(f"{n:>12,} | {fast:>8} | {str(brute):>8} | {match:>6} | {elapsed:>10.3f}")