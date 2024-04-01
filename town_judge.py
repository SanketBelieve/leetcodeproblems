n = 3
trust = [[1,3],[2,3],[3,1]]
t_count=[0]*(n+1)
for a,b in trust:
    t_count[a]-=1
    t_count[b]+=1
for i in range(1,n+1):
    if t_count[i] == n - 1:  # Check if a person is trusted by everyone except themselves
            print(i)
        
print(-1)
            

    
       
        
