# https://app.codility.com/programmers/lessons/15-caterpillar_method/count_triangles/
def solution(A):
    if not A or len(A) < 3:
        return 0
    A.sort()
    # print(A) 
    N = len(A)
    count = 0
    for X in range(N - 2) :
        Z = X + 2
        for Y in range(X + 1, N - 1) :
            while Z < N and A[X] + A[Y] > A[Z]:
                Z += 1
            count += Z - Y - 1
            # if Z > Y + 1 :
            #     print(f"\nX={X} Y={Y} Z={Z}")
            #     print(f"count={count}")
                
            # print(f"A[{X}]={A[X]} A[{Y}]={A[Y]} A[{Z}]={A[Z]}")
                
    return count 