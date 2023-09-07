month = input()
booked_nights = int(input())

flat_rent = 0
studio_rent = 0

if month == 'May' or month == 'October':
    if 7 < booked_nights <= 14:
        studio_rent = (booked_nights * 50) * 0.95
        flat_rent = booked_nights * 65
    elif booked_nights > 14:
        studio_rent = (booked_nights * 50) * 0.70
        flat_rent = (booked_nights * 65) * 0.90
    else:
        studio_rent = booked_nights * 50
        flat_rent = booked_nights * 65



elif month == 'June' or month == 'September':
    if booked_nights > 14:
        studio_rent = (booked_nights * 75.20) * 0.80
        flat_rent = (booked_nights * 68.70) * 0.90
    else:
        studio_rent = booked_nights * 75.20
        flat_rent = booked_nights * 68.70



elif month == 'July' or month == 'August':
    if booked_nights > 14:
        studio_rent = booked_nights * 76
        flat_rent = (booked_nights * 77) * 0.90
    else:
        studio_rent = booked_nights * 76
        flat_rent = booked_nights * 77


print(f"Apartment: {flat_rent:.2f} lv.")
print(f"Studio: {studio_rent:.2f} lv.")