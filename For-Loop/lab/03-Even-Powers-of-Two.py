import math

number_input = 3

for power in range(0, number_input + 1, 2):
    result = math.pow(2, power)
    print(round(result))