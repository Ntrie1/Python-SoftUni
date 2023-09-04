length = int(input())
width = int(input())
height = int(input())
percent = float(input())

tank_volume = length * width * height
liters_volume = tank_volume / 1000
occupied_space = percent / 100

liters_required = liters_volume * (1 - occupied_space)

print(liters_required)