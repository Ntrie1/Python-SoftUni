# Четем час и минути от потребителя
hours = int(input())
minutes = int(input())

# Добавяме 15 минути към времето
minutes += 15

# Проверяваме дали минутите са над 59
if minutes >= 60:
    minutes -= 60
    hours += 1

# Проверяваме дали часовете са над 23
if hours > 23:
    hours = 0

# Извеждаме резултата в желания формат
print(f"{hours}:{minutes:02}")