needed_nylon = int(input())
needed_dye = int(input())
needed_thinner = int(input())
hours_work_needed = int(input())

nylon = 1.50
dye = 14.50
thinner = 5.00
plasticBag = 0.40

nylonPrice =(needed_nylon + 2) * nylon
dyePrice = (needed_dye + (needed_dye * 0.1)) * dye
thinnerPrice = needed_thinner * thinner

allMaterialsPrice = nylonPrice + dyePrice + thinnerPrice + plasticBag
priceForWorkers = (allMaterialsPrice * 0.3) * hours_work_needed
finalPrice = allMaterialsPrice + priceForWorkers
print(finalPrice)