poultryMenuPrice = 10.35
fishMenuPrice = 12.40
veggieMenuPrice = 8.15

deliveryPrice = 2.50

poultryOrdered = int(input())
fishOrdered = int(input())
veggieOrdered = int(input())

poultryPrice = poultryOrdered * poultryMenuPrice
fishPrice = fishOrdered * fishMenuPrice
veggiePrice =  veggieOrdered * veggieMenuPrice

sumPrice = poultryPrice + fishPrice + veggiePrice

dessert = sumPrice * 0.2

finalPrice = sumPrice + dessert + deliveryPrice

print(finalPrice)
