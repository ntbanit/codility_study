# https://app.codility.com/programmers/lessons/13-fibonacci_numbers/ladder/
def solution(A, B):
    max_number = max(A)
    ways = [i for i in range(max_number + 1)]
    MAX_MOD = 2 ** 30
    for i in range(4, max_number + 1):
        ways[i] = (ways[i - 1] + ways[i - 2]) % MAX_MOD 
        # if i < 100:
        #     print(f"i={i} ways[i]={ways[i]}")
    output = []
    for X, Y in zip(A, B) :
        way_mod = ways[X] % (2 ** Y)
        # print(f"X={X} ways[X]={ways[X]}")
        output.append(way_mod)
    return output