letters = ["c","f","j"]
target = "c"
for i in letters:
    if i > target:
        print(i)
        break
    elif i==target:
        print(i)
        
    else:
        print(letters[0])
        break