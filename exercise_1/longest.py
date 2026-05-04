def solution(S):
    def valid(password) :
        letters = digits = 0
        for c in password :
            if '0' <= c <= '9':
                digits += 1
            elif 'a' <= c <= 'z' or 'A' <= c <= 'Z' :
                letters += 1
            else :
                return 0
        if letters % 2 == 0 and digits % 2 == 1 :
            return letters +digits
        return 0
    words = S.split(' ')
    
    output = 0
    for word in words : 
        output = max(output, valid(word))
            
    return output