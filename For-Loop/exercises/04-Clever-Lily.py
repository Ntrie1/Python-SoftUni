age = int(input())
price = float(input())
toy_p = int(input())

money = 0
toy_count = 0
years = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money += 10 + (toy_count - 1) * 10
        years += 1
    else:
        toy_count += 1

collected_money = (money - years) + (toy_count * toy_p)
if collected_money >= price:
    print(f'Yes! {collected_money - price:.2f}')
else:
    print(f'No! {price - collected_money:.2f}')
