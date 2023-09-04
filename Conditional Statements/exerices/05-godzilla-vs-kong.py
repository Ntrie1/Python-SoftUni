movie_budget = float(input())
extras_count = int(input())
clothes_price = float(input())

director_price = movie_budget * 0.10

if extras_count > 150:
   clothes_price -= clothes_price * 0.10



all_clothes_price = extras_count * clothes_price
needed_money = director_price + all_clothes_price
result = abs(movie_budget - needed_money)

if needed_money > movie_budget:
    print('Not enough money!')
    print(f'Wingard needs {result:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {result:.2f} leva left.')