n=(input("enter a num"))
t=len(n)
a=int(n)
b=a
res=0
while (b>=1):
    res=res+pow(b%10,t)

    b=int(b/10)
if(res==a):
    print("armstrong")
else:
    print("not a armstrong")    