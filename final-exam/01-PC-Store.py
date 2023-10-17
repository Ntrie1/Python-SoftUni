cpu_price = float(input())
video_card_price = float(input())
ram_price = float(input())
ram_amount = int(input())
discount = float(input())

cpu_price_lv = cpu_price * 1.57
video_card_price_lv = video_card_price * 1.57
ram_price_lv = ram_price * 1.57
final_ram_price = ram_price_lv * ram_amount

cpu_price_discounted = cpu_price_lv - (cpu_price_lv * discount)
video_card_price_discounted = video_card_price_lv - (video_card_price_lv * discount)

final_sum_price = cpu_price_discounted + video_card_price_discounted + final_ram_price
print(f"Money needed - {final_sum_price:.2f} leva.")

