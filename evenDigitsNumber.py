def solution(a):
    
    counter = 0 
    
    for num in a:
        if len(str(num)) % 2 == 0:
            counter +=1
            
    return counter
    