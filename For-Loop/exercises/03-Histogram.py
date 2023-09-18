count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

n = int(input())

for _ in range(n):
    number = int(input())

    if number < 200:
        count_p1 += 1
    elif 200 <= number <= 399:
        count_p2 += 1
    elif 400 <= number <= 599:
        count_p3 += 1
    elif 600 <= number <= 799:
        count_p4 += 1
    else:
        count_p5 += 1


total = count_p1 + count_p2 + count_p3 + count_p4 + count_p5

p1_percentage = (count_p1 / total) * 100
p2_percentage = (count_p2 / total) * 100
p3_percentage = (count_p3 / total) * 100
p4_percentage = (count_p4 / total) * 100
p5_percentage = (count_p5 / total) * 100


print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")



