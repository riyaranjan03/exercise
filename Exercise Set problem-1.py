def mem(n,a):
    d1=(n)*(15/100)
    d2=(n)*(8/100)
    if a=="yes":
        return (n-(d1+d2))
    else:
       return (n-d2)
    
n=int(input('cost of your item: '))
a=input('are you a prime member? yes or no: ')
print(mem(n,a))
