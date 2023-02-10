k=list(int(input("enter a number")))
def armstrong(n):
     t=len(n)
     a=int(n)
     b=a
     res=0
     while( b>=1):
        res=res+pow(b%10,t)
        b=int(b/10)
     if(res==a):
        return True
     else:
        return False
     for i in range(len(k)):
        if(armstrong(k[i])):
            print(k[i])
    
