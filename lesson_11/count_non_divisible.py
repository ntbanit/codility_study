# https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_non_divisible/
from collections import Counter, defaultdict
def solution(A):
    N = len(A)
    counter = Counter(A)
    # print(counter)
    index_map = defaultdict(list)
    for i in range(N):
        index_map[A[i]].append(i) 
    # print(index_map)

    output = [0] * N
    for key in counter :
        cnt = N
        seen = set()
        for i in range(1, int(key ** 0.5) + 2) :
            if key % i != 0 :
                continue 
            for j in [i, key // i]:
                if j in counter and j not in seen:
                    # print(f"key={key} i={i} j={j}")
                    cnt -= counter[j]
                    seen.add(j)
        # print(f"key={key} cnt={cnt}")
        for i in index_map[key]:
            output[i] = cnt

    return output 