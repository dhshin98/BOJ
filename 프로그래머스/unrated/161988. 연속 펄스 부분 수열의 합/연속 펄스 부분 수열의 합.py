def solution(sequence):

    answer = -100000
    s1 = s2 = s1_min = s2_min = 0
    one = 1
    
    # s1 [1,-1,..]
    # s2 [1,-1,..]
    
    for i in range(len(sequence)):
        s1 += sequence[i] * one 
        s2 += sequence[i] * (-one)
        
        s1_min = min(s1_min,s1)
        s2_min = min(s2_min,s2)
    
        answer = max(answer, s1-s1_min, s2-s2_min)
    
        one *= -1
    
    return answer