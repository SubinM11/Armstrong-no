#armstrong 

n=153
s=n
sum=0
b=len(str(n))

while n!=0:
    r=n%10
    sum=sum+(r**b)
    n=n//10

if s==sum:
    print(s,"armstrong")
else:
    print(s,"not armstrong")    