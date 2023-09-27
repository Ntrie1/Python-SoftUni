max_number = float('-inf')

while True:
    command = input()

    if command == "Stop":
        break

    number = float(command)

    if number > max_number:
        max_number = number

print("%d" % max_number)
