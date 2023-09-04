import math

series = input()
episode = int(input())
break_time = int(input())

lunch_duration = 1 / 8 * break_time
leisure_duration = 1 / 4 * break_time

total_busy_time = lunch_duration + leisure_duration
left_time = break_time - total_busy_time

if left_time >= episode:
    print(f'You have enough time to watch {series} and left with {math.ceil(left_time - episode)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(episode-left_time)} more minutes.")
