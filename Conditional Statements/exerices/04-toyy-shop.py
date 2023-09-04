holiday_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddybear_count = int(input())
minions_count = int(input())
lorry_count = int(input())


total_puzzle_price = puzzle_count * 2.60
total_doll_price = doll_count * 3
total_teddybear_price = teddybear_count * 4.10
total_minions_price = minions_count * 8.20
total_lorry_price = lorry_count * 2

all_toys_count = puzzle_count + doll_count + teddybear_count + minions_count + lorry_count
total_price = total_puzzle_price + total_doll_price + total_teddybear_price + total_minions_price + total_lorry_price


discount = 0

if all_toys_count >= 50:

 discount = 0.25 * total_price
total_price = total_price - discount


rent_price = 0.10 * total_price
total_price = total_price - rent_price


if total_price >= holiday_price:

 print(f'Yes! {total_price - holiday_price:.2f} lv left.')

else:
    print(f'Not enough money! {holiday_price - total_price:.2f} lv needed.')




