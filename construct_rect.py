import math
def constructRectangle( area: int) -> list[int]:
        width=int(math.sqrt(area))
        length=int(math.ceil(area/width))

        while width*length != area:
            if width*length< area:
                length+=1
            else:
                width-=1
        return [length,width]  

s=122122
print(constructRectangle(s))    
              