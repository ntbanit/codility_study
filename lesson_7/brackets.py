# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets
def solution(S):
    stack = []
    my_map = {')': '(', ']': '[', '}': '{'}
    for ch in S :
        if ch in '({[': 
            stack.append(ch)
        elif not stack or stack.pop() != my_map[ch]: # open_bracket
            return 0
    return 1 if not stack else 0