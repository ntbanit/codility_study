# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
def solution(S, P, Q):
    nucleotides = ('A', 'C', 'G', 'T')
    N = len(S) 
    nuc_prefix = [[0, 0, 0, 0]]
    for i in range(N) :
        for j in range(4) : 
            if S[i] == nucleotides[j]:
                curr = nuc_prefix[-1][:]
                curr[j] += 1
                nuc_prefix.append(curr)
                break
    # print(nuc_prefix)

    output = []
    for i in range(len(P)):
        left, right = P[i], Q[i]
        for j in range(4) : 
            diff = nuc_prefix[right + 1][j] - nuc_prefix[left][j]
            # print(f"left={left} right={right} j={j} diff={diff}")
            if diff != 0:
                output.append(j + 1)
                break

    return output