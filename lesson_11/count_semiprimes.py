# https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_semiprimes/
def seive(N) :
    if N <= 3 :
        return [0] * (N + 1)
        
    prime = [True] * (N + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(N**0.5) + 2) :
        if not prime[i]:
            continue

        for j in range(i * i, N + 1, i) :
            prime[j] = False
    
    prime_list = [i for i in range(2, N + 1) if prime[i]]
    # print(prime_list)
    # print(len(prime_list))
    # print(5133 ** 2)
    NN = len(prime_list)
    semiprime_set = set()
    for i in range(NN) :
        for j in range(i, NN) :
            if prime_list[i] * prime_list[j] > N :
                break
            semiprime_set.add(prime_list[i] * prime_list[j])

    semiprime_prefix = [0] * (N + 1)
    for i in range(4, N + 1) :
        semiprime_prefix[i] = semiprime_prefix[i - 1]
        if i in semiprime_set :
            semiprime_prefix[i] += 1
    
    return semiprime_prefix

def solution(N, P, Q):
    semiprime_prefix = seive(N)
    # print(semiprime_prefix)
    output = []
    for i in range(len(P)) :
        semi_cnt = semiprime_prefix[Q[i]] - semiprime_prefix[P[i] - 1]
        output.append(semi_cnt)
    return output