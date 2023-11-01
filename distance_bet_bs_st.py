distance = [1,2,3,4]
start = 0
destination = 1
circle=sum(distance)
if start==destination:
    print(0)
elif start < destination:
    trip= sum(distance[start:destination])
else:
    trip = sum(distance[destination:start]) 

if circle-trip > trip:
    print(trip)  
else:
    print(circle-trip)  
    
def distanceBetweenBusStops(distance: list[int], start: int, destination: int) -> int:
    if start == destination:
        return 0
    elif start < destination:
        trip = sum(distance[start:destination])
    else:
        trip = sum(distance[destination:start])

    circle = sum(distance)

    if circle - trip > trip:
        return trip
    return circle - trip        

           