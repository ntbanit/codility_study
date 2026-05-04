# https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/
def solution(K, A) :
    count = 0
    tied_rope = 0
    for rope in A :
        if tied_rope >= K :
            count += 1
            tied_rope = rope 
        else :
            tied_rope += rope 
    
    if tied_rope >= K :
            count += 1
    
    return count 