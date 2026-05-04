# https://app.codility.com/programmers/trainings/1/longest_password/
def solution(S):
    def valid(password) :
        letters = digits = 0
        for c in password :
            if '0' <= c <= '9':
                digits += 1
            elif 'a' <= c <= 'z' or 'A' <= c <= 'Z' :
                letters += 1
            else :
                return -1
        if letters % 2 == 0 and digits % 2 == 1 :
            return letters + digits
        return -1
    words = S.split(' ')
    # print(words)
    output = -1
    for word in words : 
        cnt = valid(word)
        # print(f"word={word} cnt={cnt}")
        output = max(output, cnt)
            
    return output