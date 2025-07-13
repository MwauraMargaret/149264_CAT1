class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{book.title} borrowed successfully.")
        else:
            print(f"{book.title} is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{book.title} returned successfully.")
        else:
            print("This book was not borrowed by you.")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            for book in self.borrowed_books:
                print(f"{book.title} by {book.author}")


if __name__ == "__main__":
    book1 = Book("Americanah", "Chimamanda Ngozi")
    book2 = Book("Facing Mount Kenya", "Jomo Kenyatta")

    member = LibraryMember("John", "BBT001")

    while True:
        print("\n1. Borrow Book\n2. Return Book\n3. List Borrowed Books\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            if title == book1.title:
                member.borrow_book(book1)
            elif title == book2.title:
                member.borrow_book(book2)
            else:
                print("Book not found.")

        elif choice == '2':
            title = input("Enter book title: ")
            if title == book1.title:
                member.return_book(book1)
            elif title == book2.title:
                member.return_book(book2)
            else:
                print("Book not found.")

        elif choice == '3':
            member.list_borrowed_books()

        elif choice == '4':
            break
        else:
            print("Invalid option.")
