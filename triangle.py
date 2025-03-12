#calculate the 1+2+...+n
n=int(input())
T=0
for i in range(n+1):
    T+=i
print("T"+str(n)+"="+str(int(T)))