cubic_meters = float(input())

initalPrice = cubic_meters * 7.61
discount = 0.18 * initalPrice
finalPrice = initalPrice - discount

print(f'The final price is: {finalPrice} lv.')
print(f'The discount is: {discount} lv.')