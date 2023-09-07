budget = float(input())
season = input()

vacation_price = 0
destination = ''
place_info = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation_price = budget * 0.30
        place_info = 'Camp - '
    else:
        vacation_price = budget * 0.70
        place_info = 'Hotel - '


elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vacation_price = budget * 0.40
        place_info = 'Camp - '
    else:
        vacation_price = budget * 0.80
        place_info = 'Hotel - '


else:
    destination = 'Europe'
    vacation_price = budget * 0.90
    place_info = 'Hotel - '

print(f"Somewhere in {destination}")
print(f"{place_info}{vacation_price:.2f}")
