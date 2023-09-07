N1 = int(input())
N2 = int(input())
operator = input()


def is_even(number):
    return number % 2 == 0


if operator == "+":
    result = N1 + N2
    print(f"{N1} {operator} {N2} = {result} - {'even' if is_even(result) else 'odd'}")
elif operator == "-":
    result = N1 - N2
    print(f"{N1} {operator} {N2} = {result} - {'even' if is_even(result) else 'odd'}")
elif operator == "*":
    result = N1 * N2
    print(f"{N1} {operator} {N2} = {result} - {'even' if is_even(result) else 'odd'}")
elif operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
elif operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
else:
    print("Invalid operator")
