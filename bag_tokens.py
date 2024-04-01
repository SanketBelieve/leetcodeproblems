tokens = [100]
power = 50

res=scr=0
l,r=0,len(tokens)-1
tokens.sort()

while l<=r:
    if power >= tokens[l]:
        power -= tokens[l]
        l+=1
        scr+=1
        res=max(res,scr)
    elif scr > 0:
        power+=tokens[r]
        r-=1
        scr -= 1
    else:
        break
print(res)            