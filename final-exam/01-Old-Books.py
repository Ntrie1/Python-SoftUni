favourite_book = input()

checked_books = 0
is_book_found = False

books = input()
while books != 'No More Books':
    if books == favourite_book:
        is_book_found = True
        print(f"You checked {checked_books} books and found it.")
        break

    checked_books += 1
    books = input()

if not is_book_found:
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")
