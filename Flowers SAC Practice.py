#Matthew's Epic Coding Piece That Is Awesome.
#Flowers price listings

priceList = {
    'Vandas' : 7.35,
    'Miltonia' : 9.80,
    'Cattleya' : 10.00
}

while True:
    member = input('[Y]/[N] Member? ')
    if member == "Y":
        member = True
        break
    elif member == "N":
        member = False
        break
    else:
        print('Please enter a proper letter.')

orchid = input('[V]andas, [M]iltonia, or [C]attleya?')
if orchid not in ['V','M','C']:
    print("Please enter V, M or C next time.")
    exit()

quant = int(input("How many of the flower type? (0-99) "))
if quant > 99 or quant < 1:
    print("Please enter a vaild number.")
    exit()
else:
    pass

price = quant * orchid
if orchid == "V":
    price = priceList['Vandas']
    price = int(price) * int(quant)
    if quant > 5:
        price = price *0.95
    if member == True:
        price = price *0.9
        print("Your price is:", price)
    if member == False:
        print("your price is:", price)

elif orchid == "M":
    price = priceList['Miltonia']
    price = int(price) * int(quant)
    if quant > 5:
        price = price *0.95
    if member == True:
        price = price *0.9
        print("Your price is:", price)
    if member == False:
        print("your price is:", price)

elif orchid == "C":
    price = priceList['Cattleya']
    price = int(price) * int(quant)
    if quant > 5:
        price = price *0.95
    if member == True:
        price = price *0.9
        print("Your price is:", price)
    if member == False:
        print("your price is:", price)
