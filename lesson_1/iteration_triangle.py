def triangle(n: int) :
    for i in range(0, n):
        line = []
        for j in range(n - i):
            line.append(' ')
        for j in range(2 * i - 1) :
            line.append('*')
        print(''.join(line))

triangle(5)