# Swap the Elements Problem
## Problem
You are given an integer `m` (1 ≤ m ≤ 1,000,000) and two non‑empty, zero‑indexed arrays **A** and **B** of `n` integers,`a₀, a₁, …, aₙ₋₁` and `b₀, b₁, …, bₙ₋₁` respectively (0 ≤ aᵢ, bᵢ ≤ m).
The goal is to check whether there is a **swap operation** which can be performed on these arrays such that the sum of elements in array **A** equals the sum of elements in array **B** after the swap.
By *swap operation* we mean picking one element from array **A** and one element from array **B** and exchanging them.

---
## Solution O(n²)
The simplest method is to swap every pair of elements and calculate the totals.
Using that approach gives us **O(n³)** time complexity.
A better approach is to calculate the sums of elements at the beginning and check only how the totals change during the swap operation.
### 4.2: Swap the elements — O(n²)

```python
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
```

---
## Solution O(n + m)
The best approach is to count the elements of array **A** and calculate the difference `d`between the sums of the elements of arrays **A** and **B**.
For every element of array **B**, we assume that we will swap it with some element from array **A**. The difference `d` tells us the value from array **A** that we are interested in swapping, because only one value will cause the two totals to be equal.
The occurrence of this value can be found in constant time from the array used for counting.

### 4.3: Swap the elements — O(n + m)

```python
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
    count = counting(A, m)

    for i in range(n):
        if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
            return True

    return False
```
