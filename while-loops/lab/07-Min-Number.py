min_number = float('inf')

while True:
    command = input()

    if command == 'Stop':
        break

    number = float(command)

    if number < min_number:
        min_number = number

print("%d" % min_number)
