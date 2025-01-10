def display_book_info(book_id, title, author, availability=True):
    status = "Available" if availability else "Checked Out"
    print(f"Book ID: {book_id}, Title: {title}, Author: {author}, Status: {status}")

def add_book(books, book_id, title, author):
    if book_id not in books:
        books[book_id] = [title, author, True]
        print(f"Book '{title}' added successfully.")
    else:
        print("Book ID already exists.")

def remove_book(books, book_id):
    if book_id in books:
        removed_book = books.pop(book_id)
        print(f"Book '{removed_book[0]}' removed successfully.")
    else:
        print("Book ID not found.")

def check_out_book(books, book_id):
    if book_id in books:
        if books[book_id][2]:
            books[book_id][2] = False
            print(f"Book '{books[book_id][0]}' checked out successfully.")
        else:
            print(f"Book '{books[book_id][0]}' is already checked out.")
    else:
        print("Book ID not found.")

def return_book(books, book_id):
    if book_id in books:
        if not books[book_id][2]:
            books[book_id][2] = True
            print(f"Book '{books[book_id][0]}' returned successfully.")
        else:
            print(f"Book '{books[book_id][0]}' was not checked out.")
    else:
        print("Book ID not found.")

def display_all_books(books):
    if not books:
        print("No books available in the library.")
    else:
        for book_id, book_info in books.items():
            display_book_info(book_id, book_info[0], book_info[1], book_info[2])

# Sample interaction with the library management system
if __name__ == "__main__":
    books = {}

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Check Out Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            add_book(books, book_id, title, author)
        elif choice == "2":
            book_id = input("Enter Book ID to remove: ")
            remove_book(books, book_id)
        elif choice == "3":
            book_id = input("Enter Book ID to check out: ")
            check_out_book(books, book_id)
        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            return_book(books, book_id)
        elif choice == "5":
            display_all_books(books)
        elif choice == "6":
            print("Exiting... Thank you for using the library management system.")
            break
        else:
            print("Invalid choice. Please try again.")
