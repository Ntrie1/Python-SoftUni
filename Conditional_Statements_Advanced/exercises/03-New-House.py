flower_type = input()
flower_count = int(input())
budget = int(input())

price = 0

if flower_type == 'Roses':
    price = flower_count * 5
    if flower_count > 80:
        price = price * 0.90

elif flower_type == 'Dahlias':
    price = flower_count * 3.80
    if flower_count > 90:
        price *= 0.85

elif flower_type == 'Tulips':
    price = flower_count * 2.80
    if flower_count > 80:
        price *= 0.85


elif flower_type == 'Narcissus':
    price = flower_count * 3
    if flower_count < 120:
        price *= 1.15


elif flower_type == 'Gladiolus':
    price = flower_count * 2.50
    if flower_count < 80:
        price *= 1.20

difference_money = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {difference_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference_money:.2f} leva more.")
