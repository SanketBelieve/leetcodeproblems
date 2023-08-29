'''
def bestClosingTime( customers: str) -> int:
    p=0
    for i in customers:
        if i=='Y':
            p+=1
        elif i=='N':
            p+=0                  
    return p    

print(bestClosingTime('YYNY'))
'''
def bestClosingTime( customers: str) -> int:
        max_score = score = 0
        best_hour = -1

        for i, c in enumerate(customers):
            score += 1 if c == 'Y' else -1
            if score > max_score:
                max_score, best_hour = score, i
                
        return best_hour + 1
