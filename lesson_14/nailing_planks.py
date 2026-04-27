# https://app.codility.com/programmers/lessons/14-binary_search_algorithm/nailing_planks/

def solution(A, B, C):
    N, M = len(A), len(C)
    min_max_abc = min(max(B), max(C))
    
    def check(J):
        if J == 0 :
            return False 
        # with each candidate J, only check first J nail 
        pos_set = set(C[pos] for pos in range(J) )
        # rebuil the prefix each time check a J
        prefix = [0] * (min_max_abc + 1) 
        for pos in range(min_max_abc + 1) :
            prefix[pos] = prefix[pos - 1]
            prefix[pos] += 1 if pos in pos_set else 0
        # print(f"J={J} pos_set={pos_set}")
        # print(f"prefix={prefix}")
        for start, end in zip(A, B) :
            if end >= min_max_abc + 1 :
                return False
            # print(f"start={start} end={end} prefix_range={prefix[end] - prefix[start - 1]}")
            if prefix[end] - prefix[start - 1] == 0:
                return False
        return True

    left, right = 0, M
    answer = -1
    while left <= right :
        mid = (left + right) // 2
        if check(mid):
            answer = mid 
            right = mid - 1
        else:
            left = mid + 1
    return answer