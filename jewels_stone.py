jewels = "aA"
stones = "aAAbbbb"

cnt=0
for i in stones:
    for j in jewels:
        if i==j:
            cnt+=1
print(cnt)            