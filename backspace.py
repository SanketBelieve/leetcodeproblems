s = "ab#c"
t = "ad#c"

s_out=[]
t_out=[]

for char in s:
    if char=='#':
        if s_out:s_out.pop()
    else:
        s_out.append(char)   
for char in t:
    if char=='#':
        if t_out:t_out.pop()
    else:
        t_out.append(char)   
        
if s_out==t_out:
    print(True)
else:
    print(False)                      