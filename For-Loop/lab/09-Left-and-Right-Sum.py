n = int(input())

left_sum = 0
right_sum = 0

for _ in range(n):
    num = int(input())
    left_sum += num

for _ in range(n):
    num = int(input())
    right_sum += num

difference = abs(left_sum - right_sum)

if difference == 0:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")
