# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
def solution(H):
    stack = []
    count = 0
    for height in H : 
        # Pop all blocks that are taller than current height
        # (those blocks have ended and can't extend further)
        while stack and stack[-1] > height :
            stack.pop()
        
        # Only start a new block if this height isn't already "active"
        if not stack or stack[-1] < height :
            stack.append(height)
            count += 1
        # If stack[-1] == h, the existing block simply continues — no new block needed
        
    return count 