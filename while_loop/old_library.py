searched_book = input()
searched_book_count = 0

while True:
    book = input()

    if book == searched_book:
        print(f"You checked {searched_book_count} books and found it.")
        break

    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {searched_book_count} books.")
        break

    searched_book_count += 1
