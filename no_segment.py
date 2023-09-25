'''s = "Hello, my name is John"
cnt=0
for i in s:
    
    if i==" " or i=="," in s:
        cnt+=1
        print(cnt)'''
def countSegments( s: str) -> int:
    cnt=[]
    if (len(s))==0:
        return(0)
    else:
        k=s.split(" ")
        for j in k:
            if len(j)!=0:
                cnt.append(j)
        return (len(cnt))            

print(countSegments("Hello, my name is John"))    