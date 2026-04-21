#https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
def solution(X, Y, D):
    N = (Y - X + D - 1) // D  
    return N
