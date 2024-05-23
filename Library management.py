class BOOKS:
    def __init__(self, title, author, isbn, publication_data, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_data = publication_data
        self.copies = copies

books = []

def Add_book():
    title = input("Book title: ")
    author = input("the writer: ")
    isbn = input("International Standard Book Number: ")
    publication_data = input("Release date: ")
    copies = int(input("the number of available copies: "))

    new_book = BOOKS (title, author, isbn, publication_data, copies)
    books.append(new_book)
    print(f"Book '{title}' added successfully")

def search_books():
    search_term = input("Search by title, author, or ISBN: ")

    result = list(filter(lambda book: search_term.lower() in book.title.lower() 
                          or search_term.lower() in book.author.lower() 
                          or search_term.lower() in book.isbn.lower(), books))

    if result:
        print("Search result:")
        for book in result:
            print(f"- {book.title} by {book.author}")
    else:
        print("No matching books found")

def show_book_details(book):
    print("\nBook information:")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"ISBN: {book.isbn}")
    print(f"Release Date: {book.publication_data}")
    print(f"Copies: {book.copies}")

def edit_book(book):
    new_title = input("Enter new title: ")
    new_author = input("Enter new author: ")
    new_isbn = input("Enter new ISBN: ")
    new_publication_data = input("Enter new release date: ")
    new_copies = input("Enter new number of copies: ")

    if new_title:
        book.title = new_title
    if new_author:
        book.author = new_author
    if new_isbn:
        book.isbn = new_isbn
    if new_publication_data:
        book.publication_data = new_publication_data
    if new_copies:
        book.copies = int(new_copies)

    print(f"Book '{book.title}' successfully edited")

def delete_book(book):
    books.remove(book)
    print(f"Book '{book.title}' successfully deleted")

while True:
    print("\nHome book management system")
    print("1. Add book")
    print("2. Search book")
    print("3. Show book information")
    print("4. Edit book information")
    print("5. Remove book")
    print("6. Sign out")

    choice = input("Enter your choice: ")

    if choice == "1":
        Add_book()
    elif choice == "2":
        search_books()
    elif choice == "3":
        if not books:
            print("There are no books in the library")
            continue
        isbn = input("Enter ISBN of the book: ")
        book = next((book for book in books if book.isbn == isbn), None)
        if book:
            show_book_details(book)
        else:
            print(f"No book with ISBN '{isbn}' found")
    elif choice == "4":
        if not books:
            print("There are no books in the library")
            continue
        isbn = input("Enter ISBN of the book to edit: ")
        book = next((book for book in books if book.isbn == isbn), None)
        if book:
            edit_book(book)
    elif choice == "5":
        if not books:
            print("There are no books in the library")
            continue
        isbn = input("Enter ISBN of the book to delete: ")
        book = next((book for book in books if book.isbn == isbn), None)
        if book:
            delete_book(book)
        else:
            print(f"No book with ISBN '{isbn}' found")
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")