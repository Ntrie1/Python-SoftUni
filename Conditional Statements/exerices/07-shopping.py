budget = float(input())
videocard = int(input())
processor = int(input())
ram_memory = int(input())

videocard_sum_price = videocard * 250
processor_sum_price = processor * (videocard_sum_price * 0.35)
ram_sum_price = ram_memory * (videocard_sum_price * 0.1)

final_price = videocard_sum_price + processor_sum_price + ram_sum_price

if videocard > processor:
    final_price = final_price - (final_price * 0.15)


if budget >= final_price:
    remained_money = budget - final_price
    print(f'You have {remained_money:.2f} leva left!')
else:
    needed_money = final_price - budget
    print(f'Not enough money! You need {needed_money:.2f} leva more!')
