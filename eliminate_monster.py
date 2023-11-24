dist = [1,3,4]
speed = [1,1,1]

def eliminateMaximum( dist: list[int], speed: list[int]) -> int:
    minReach=[]
    for d,s in zip(dist,speed):
        minute=math.ceil(d/s)
        minReach.append(minute)
    minReach.sort()
    res=0
    for minute in range(len(minReach)):
        if minute >= minReach[minute]:
            return res
        res+=1
    return res        
