import math

absent_days = int(input())
food_in_kilos = int(input())
food_for_first_deer = float(input())
food_for_second_deer = float(input())
food_for_third_deer = float(input())

first_deer_needed_food = absent_days * food_for_first_deer
second_deer_needed_food = absent_days * food_for_second_deer
third_deer_needed_food = absent_days * food_for_third_deer

sum_needed_food = first_deer_needed_food + second_deer_needed_food + third_deer_needed_food

difference = abs(food_in_kilos - sum_needed_food)

if sum_needed_food <= food_in_kilos:
    print(f'{math.floor(difference)} kilos of food left.')
else:
    print(f'{math.ceil(difference)} more kilos of food are needed.')
