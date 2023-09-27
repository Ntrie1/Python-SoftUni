total_balance = 0

while True:
    command = input()

    if command == 'NoMoreMoney':
        break

    amount = float(command)

    if amount < 0:
        print('Invalid operation!')
        break

    total_balance += amount
    print(f"Increase: {amount:.2f}")


print(f"Total: {total_balance:.2f}")
