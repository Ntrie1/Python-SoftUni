weight = float(input())
serive_type = input()
distance = int(input())

base_price_per_km = 0.03

if 1 <= weight <= 10:
    base_price_per_km = 0.05
elif 10 <= weight <= 40:
    base_price_per_km = 0.10
elif 40 <= weight <= 90:
    base_price_per_km = 0.15
elif 90 <= weight <= 150:
    base_price_per_km = 0.20

express_delivery_price = 0.0

if serive_type == 'express':
    if weight < 1.0:
        express_delivery_price = 0.80
    elif 1 <= weight <= 10:
        express_delivery_price = 0.40
    elif 10 <= weight <= 40:
        express_delivery_price = 0.05
    elif 40 <= weight <= 90:
        express_delivery_price = 0.02
    elif 90 <= weight <= 150:
        express_delivery_price = 0.01
    express_delivery_price *= base_price_per_km

total_price = (base_price_per_km + weight * express_delivery_price) * distance

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_price:.2f} lv.")