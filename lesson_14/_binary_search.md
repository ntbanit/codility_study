[Link] https://codility.com/media/train/12-BinarySearch.pdf

# The problem: 
Given n binary values (1=hole, 0=no hole) and k boards of the same size, find the minimal board size that allows all holes to be covered.

**Test Case 1 — Simple**
```
n=6, k=1
Array: [0, 1, 0, 0, 1, 0]
         0  1  2  3  4  5
```
Holes at positions 1 and 4. With **1 board**, you need it to cover both → minimum size = **4** (place board at pos 1, covers 1–4).

---

**Test Case 2 — More boards**
```
n=6, k=2
Array: [0, 1, 0, 0, 1, 0]
```
Same holes, but now **2 boards** → you can cover each hole separately → minimum size = **1**.

---

**Test Case 3 — Clustered holes**
```
n=8, k=2
Array: [1, 1, 0, 0, 0, 1, 1, 0]
         0  1  2  3  4  5  6  7
```
Cluster A: positions 0–1. Cluster B: positions 5–6.
With 2 boards, cover each cluster → minimum size = **2**.

---

**Test Case 4 — All holes**
```
n=5, k=2
Array: [1, 1, 1, 1, 1]
```
With 2 boards: one covers 0–2 (size 3), one covers 3–4 → minimum size = **3**.
With size 2: board 1 covers 0–1, board 2 covers 2–3, hole at 4 uncovered ❌ — need size **3**.

---

**Test Case 5 — No holes**
```
n=5, k=1
Array: [0, 0, 0, 0, 0]
```
No holes → minimum size = **0** (or 1 depending on implementation).

---

**How the binary search works on Test Case 3:**
```
Search range: [1, 8]
Try size 4 → board 1 covers 0–3, board 2 covers 5–8 ✅ → try smaller
Try size 2 → board 1 covers 0–1, board 2 covers 5–6 ✅ → try smaller  
Try size 1 → board 1 covers 0, board 2 covers 1... but hole at 5,6 uncovered ❌ → go bigger
Answer: 2
```

The key insight is that the "sufficient" sizes form a contiguous block on the right, making binary search valid.

```python 
def boards(A, k):
    n = len(A)
    beg = 1
    end = n
    result = -1
    while (beg <= end):
        mid = (beg + end) / 2
        if (check(A, mid) <= k):
            end = mid - 1
            result = mid
        else:
            beg = mid + 1
    return result

def check(A, k):
    n = len(A)
    boards = 0
    last = -1
    for i in range(n):
        if A[i] == 1 and last < i:
            boards += 1
            last = i + k - 1
    return boards
```

---

**How the greedy check works:**

`check(A, k)` answers: *"how many boards of size k do I need minimum?"*

It scans left to right and places a board **as late as possible** — only when it finds an uncovered hole. `last` tracks the rightmost index covered by the most recently placed board.

Walk through with `A = [1,1,0,0,0,1,1,0]`, `k=2`:

```
i=0: A[0]=1, last=-1 < 0 → place board, boards=1, last = 0+2-1 = 1
i=1: A[1]=1, but last=1, NOT < 1 → skip (already covered!)
i=2: A[2]=0 → skip
...
i=5: A[5]=1, last=1 < 5 → place board, boards=2, last = 5+2-1 = 6
i=6: A[6]=1, but last=6, NOT < 6 → skip (already covered!)

returns 2
```

So 2 boards of size 2 are enough → `check(A, 2) <= k` ✅

**Why greedy placing works:** When you hit an uncovered hole, the optimal move is to start the board *right there* (not earlier), which maximizes how far right it extends and covers as many future holes as possible. Starting it earlier would waste coverage on empty space to the left.