#calculation between numbers
def cal(i,a,b):
    if i>=1 and i<=7:
        if i==1:
            return "your desired output is: ", a+b
        if i==2:
            return "your desired output is: ", a-b
        if i==3:
            return "your desired output is: ", a*b
        if i==4:
           return "your desired output is: ", a/b
        if i==5:
           return "your desired output is: ", a//b
        if i==6:
           return "your desired output is: ", a%b
        if i==7:
           return "your desired output is: ", a**b
    else:
        return "invalid input"
    
i=int(input("what you wants to perform "))   
a=int(input("your input number 1 "))
b=int(input("your input number 2 "))
print(cal(i,a,b))

#conversion:
#conversion f to c
#formula c = (f-32)*(5/9)
def fun(f):
    c=(f-32)*(5/9)
    return c
f=float(input("how much is the temperature "))
print(fun(f))

#earthquake impact
def earth(n):
    if n<0:
        return " Invalid Input "
    elif n<7:
        return " Low impact "
    else:
        return " High impact "
n=int(input())
print(earth(n))

#Factor
#wind chill temperature
def temp(T,V):
    wct=35.74+(0.6215)*(T)-(35.75)*((V)**(0.16))+(0.4275*(T))*((V)**(0.16))
    return wct
T=float(input())
V=float(input())
print(temp(T,V))
