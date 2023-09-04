import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_seconds_per_meter = float(input())

time_needed = distance_in_meters * time_seconds_per_meter
time_resistance = math.floor(distance_in_meters/15) * 12.5
total_time = time_needed + time_resistance
difference = abs(total_time - record_in_seconds)

if record_in_seconds > total_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')

