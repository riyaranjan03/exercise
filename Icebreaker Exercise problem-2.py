f=float(input("Enter the frequency in Hz: "))

if f<3e9:
    print("radio waves")
elif f>=3e9 and f<3e12:
    print("microwaves")
elif f>=3e12 and f<4.3e14:
    print("infrared light")
elif f>=4.3e14 and f<7.5e14:
    print("visible light")
elif f>=7.5e14 and f<3e17:
    print("ultraviolet light")
elif f>=3e17 and f< 3e19:
    print("X-rays")
else:
    print("gamma rays")
