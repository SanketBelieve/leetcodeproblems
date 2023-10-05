s='UD'

if s=='UD' or s=='DU':
    print(True)
else:
    print(False)  
    
def judgeCircle( moves: str) -> bool:
        lr , ud = 0 , 0

        for move in moves:
            if move == 'U':
                ud += 1
            elif move == 'D':
                ud -= 1
            elif move == 'L':
                lr += 1
            elif move == 'R':
                lr -= 1

        if lr == 0 and ud == 0:
            return True      