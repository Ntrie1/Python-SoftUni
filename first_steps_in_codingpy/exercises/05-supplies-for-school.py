pencils_amount = int(input())
markers_count = int(input())
liters_of_cleanser = int(input())
precent_discount = int(input())



pencils = 5.80
markers = 7.20
cleanser_perLtr = 1.20

pencilsPrice = pencils_amount * pencils
markersPrice = markers_count * markers
cleanserPrice = liters_of_cleanser * cleanser_perLtr

sumPrice = pencilsPrice + markersPrice + cleanserPrice
finalPrice = sumPrice - (sumPrice * (precent_discount / 100))
print(finalPrice)