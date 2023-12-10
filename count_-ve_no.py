grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

flatten_list=[item for sublist in grid for item in sublist]
print(flatten_list)
p=0
for i in flatten_list:
    if i < 0:
        p+=1
print(p)        
    