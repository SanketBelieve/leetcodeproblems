n=10

if n <= 2:
    print(0)
is_prime=[True] * n
is_prime[0]=is_prime[1]=False

for i in range(2,int(n**0.5)+1):
    if is_prime[i]:
        for j in range(i*i,n,i):
            is_prime[j]=False
print(sum(is_prime)) 