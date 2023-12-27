colors = "aabaa"
neededTime = [1,2,3,4,5]
time=0

for i in range(1,len(colors)):
    if colors[i]==colors[i-1]:
       time+=min(neededTime[i],neededTime[i-1])
       neededTime[i]=max(neededTime[i],neededTime[i-1])
print(time)    
        