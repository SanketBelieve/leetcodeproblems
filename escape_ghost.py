ghosts = [[1,0],[0,3]]
target = [0,1]
d=(target[0]) + (target[1])
for i in ghosts:
    if abs(target[0]-i[0]) + abs(target[1]-i[1]) <= d:
        print(False)
else:
    print(True)    






