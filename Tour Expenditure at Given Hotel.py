def Hotel(room_type,days,price):
    if room_type=='Delux room':
        a=7500*days
        print('price of stay: ',a)
        sgst=0.09*price
        cgst=0.09*price
        tip=0.1*price
        print('SGST: ', round(sgst, 2)) 
        print('CGST: ', round(cgst, 2)) 
        print('Tip: ', round(tip, 2))
        print('Grand total for meal: ', c+sgst+cgst+tip)
    elif room_type =='Non AC room':
        a=4500*days
        print('price of stay: ', a)
        sgst=0.025*price
        cgst=0.025*price
        tip=0.1*price
        print('SGST: ', round(sgst, 2))
        print('CGST: ', round(cgst, 2)) 
        print('Tip: ', round(tip, 2))
        print('Grand total for meal:', c+sgst+cgst+tip)
    else:
        print('Invalid room Type')
a = input('Type of room: ') #room_type
b = int(input('Number of days you stayed: ')) #days
c = int(input('Total food price: ')) #price

Hotel(a,b,c)
