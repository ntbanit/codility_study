# https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog/
def fibo_list(N) :
    A = B = 1
    fibos = []
    while B <= N :
        fibos.append(B) 
        A, B = B, A + B 
    return fibos 

from collections import deque
def solution(A):
    N = len(A)
    fibos = fibo_list(N + 1) 
    # print(fibos)
    # print(graph)
    # BFS graph cost time: O(edges + nodes) <= O(27*N + N)
    queue = deque([(-1, 0)])
    seen = set([-1])
    while queue :
        node, steps = queue.popleft()
        # print(f"node={node} steps={steps}")
         # build graph on-the-fly to reduce the cost time and memory: O(len(fibo) * N) <= O(27 * N)
        if node == N:
            return steps 
        for fibo in fibos :
            neighbor = node + fibo
            if neighbor > N:
                break
            if neighbor not in seen and (neighbor == N or A[neighbor] == 1):
                queue.append((neighbor, steps + 1))
                seen.add(neighbor)
    return -1 