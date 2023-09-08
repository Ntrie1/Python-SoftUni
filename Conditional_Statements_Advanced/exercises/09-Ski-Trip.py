days = int(input())
accommodation_type = input()
rating = input()

nights = days - 1
total_price = 0

if accommodation_type == 'room for one person':
    total_price = 18 * nights

elif accommodation_type == 'apartment':
    total_price = 25 * nights

    if nights < 10:
        total_price = total_price * 0.70
    elif nights <= 15:
        total_price = total_price * 0.65
    else:
        total_price = total_price * 0.50


elif accommodation_type == 'president apartment':
    total_price = 35 * nights

    if nights < 10:
        total_price = total_price * 0.90
    elif nights <= 15:
        total_price = total_price * 0.85
    else:
        total_price = total_price * 0.80

if rating == 'positive':
    total_price *= 1.25
else:
    total_price *= 0.90

print(f'{total_price:.2f}')
