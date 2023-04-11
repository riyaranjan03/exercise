#calculation on two numbers

a =float(input())
b =float(input())
sum =a+b
print("sum is:",sum)
dif =a-b
print("The difference is:",dif)
prod =a*b
print("Multiplication is:",prod)
div =a/b
print("Division is:",div)
mod =a%b
print("Remainder is:",mod)
floor =a//b
print("Floor division is:",floor)


#conversion

f=float(input("how much is the temperature "))
c=(f-32)*(5/9)
print(" temperature in degree celcius is ", c)
 

#earthquake impact

n=int(input())
if n<0:
    print(" Invalid Input ")
elif n<7:
    print(" Low impact ")
else:
    print(" High impact ")
    
#wind chill temperature

T=float(input())
V=float(input())
wct=35.74+(0.6215)*(T)-(35.75)*((V)**(0.16))+(0.4275*(T))*((V)**(0.16))
print(wct)


