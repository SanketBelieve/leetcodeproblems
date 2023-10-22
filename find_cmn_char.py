words = ["bella","label","roller"]
s=[]
for i in words:
    for j in i:
        if i[j]==i[j+1]:
            s.append(i)
print(s)            