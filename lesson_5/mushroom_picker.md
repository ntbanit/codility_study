# Problem
You are given a non-empty, zero-indexed array **A** of **n** (1 ≤ n ≤ 100 000) integers **a₀, a₁, …, aₙ₋₁** (0 ≤ aᵢ ≤ 1000).
This array represents the number of mushrooms growing on the consecutive spots along a road.
You are also given integers **k** and **m**(0 ≤ k, m < n).
A mushroom picker is at spot number **k** on the road and should perform **m** moves.
In one move, the picker moves to an adjacent spot.
The picker collects all the mushrooms growing on spots she visits.
The goal is to calculate the **maximum number of mushrooms** that the mushroom picker can collect in **m** moves.

## Example
Consider the array **A**:
```
Index:  0  1  2  3  4  5  6
A:      2  3  7  5  1  3  9
```
The mushroom picker starts at spot **k = 4** and should perform **m = 6** moves.
She might move through the spots:
```
3 → 2 → 3 → 4 → 5 → 6
```
and thereby collect:
```
1 + 5 + 7 + 3 + 9 = 25 mushrooms
```
This is the **maximum number** of mushrooms she can collect.

## Solution O(m²)
Note that the best strategy is to move in **one direction**, optionally followed by some moves in the **opposite direction**.
In other words, the mushroom picker should **not change direction more than once**.
With this observation, we can find the simplest solution:
- Make the first **p = 0, 1, 2, …, m** moves in one direction
- Then make the remaining **m − p** moves in the opposite direction
This is just a simple simulation of the moves of the mushroom picker,  
which requires **O(m²)** time.

## Solution O(n + m)
A better approach is to use **prefix sums**.
If we make **p** moves in one direction, we can calculate the maximal opposite location of the mushroom picker.
The mushroom picker collects all mushrooms between these extreme points.
We can calculate the total number of collected mushrooms in **constant time**
by using prefix sums.
