def fibonacci(N: int) :
    a, b = 0, 1
    result = []
    while a <= N :
        result.append(a)
        c = a + b
        a, b = b, c
    return result

print(fibonacci(100))