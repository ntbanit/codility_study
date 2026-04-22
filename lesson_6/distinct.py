# https://app.codility.com/programmers/lessons/6-sorting/distinct/
from collections import Counter 
def solution(A):
    return len(Counter(A))