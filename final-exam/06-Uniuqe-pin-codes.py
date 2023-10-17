firstNumber = int(input())
secondNumber = int(input())
thirdNumber = int(input())
outputNumber = 0
for i in range(1, firstNumber+1):
    for j in range(1, secondNumber+1):
        for k in range(1, thirdNumber+1):
            if i % 2 == 0:
                if k % 2 == 0:
                    if j == 2 or j == 3 or j == 5 or j == 7:
                        outputNumber = str(100 * i + 10 * j + k)
                        output = ' '.join(outputNumber)
                        print(output)
