annualFee = int(input())

basketball_shoes = annualFee - (annualFee * 0.4)
basketball_fit = basketball_shoes - (basketball_shoes * 0.2)
basketball_ball = basketball_fit * 0.25
basketball_accessories =  basketball_ball * 0.2

finalPrice = annualFee + basketball_shoes + basketball_fit + basketball_ball + basketball_accessories

print(finalPrice)