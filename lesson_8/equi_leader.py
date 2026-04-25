# https://app.codility.com/programmers/lessons/8-leader/equi_leader/
from collections import Counter
def solution(A):
    N = len(A)
    cnt = Counter(A) 
    candidate_leader = max(cnt, key = cnt.get) # fix 1
    count = cnt[candidate_leader]
    if count <= N // 2 :
        return 0
    
    answer = 0 
    curr = 0
    for i in range(N - 1): # fix2 S < N -1
        if A[i] == candidate_leader :
            curr += 1
        # check with any position p, 0 < p < N - 1, if the leader is the same in both sequences
        if curr > (i + 1) // 2 and (count - curr) > (N - i - 1) // 2 :
            answer += 1
    return answer 
