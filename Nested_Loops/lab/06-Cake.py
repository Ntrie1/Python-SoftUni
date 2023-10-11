cake_length = int(input())
cake_width = int(input())

cake_pieces = cake_length * cake_width
total = 0

while cake_pieces >= total:
    command = input()
    if command == 'STOP':
        break

    piece = int(command)
    total += piece

if total > cake_pieces:
    needed = total - cake_pieces
    print(f'No more cake left! You need {needed} pieces more.')
else:
    left = cake_pieces - total
    print(f'{left} pieces are left.')
