groups_budget = int(input())
season = input()
fishmen_count = int(input())

boat_price = 0
discount = 0

if season == 'Spring':
    boat_price = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_price = 4200
else:
    boat_price = 2600

if fishmen_count <= 6:
    discount = 0.10
elif fishmen_count <= 11:
    discount = 0.15
else:
    discount = 0.25

final_price = boat_price - (boat_price * discount)

if fishmen_count % 2 == 0 and season != 'Autumn':
    final_price *= 0.95


if groups_budget >= final_price:
    print(f"Yes! You have {(groups_budget - final_price):.2f} leva left.")
else:
    print(F"Not enough money! You need {abs(groups_budget - final_price):.2f} leva.")

