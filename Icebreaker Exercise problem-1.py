a=int(input('Enter the wavelength in nm: '))

if a>=380 and a<450:
    print('VIOLET')
elif a>=450 and a<495:
    print('BLUE')
elif a>=495 and a<570:
    print('GREEN')
elif a>= 570 and a<590:
    print('YELLOW')
elif a>=590 and a<620:
    print('ORANGE')
elif a>=620 and a<750:
    print('RED')
else:
    print('Inappropriate wavelength')
