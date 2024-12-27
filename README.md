

# Book Management System

This project is a Python-based book management system that allows users to add, search, display, edit, and remove books. It provides an interactive menu for performing these operations on a list of books.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [License](#license)

## Overview
This book management system is a simple command-line application where users can manage a collection of books. Users can:
- Add new books to the system
- Search for books by title, author, or ISBN
- View book details
- Edit existing book information
- Remove books from the collection

The system is built using Python's basic input/output functions and stores books in memory during the session.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/book-management-system.git
    ```

2. Navigate to the project folder:
    ```bash
    cd book-management-system
    ```

3. There are no external dependencies to install, as this is a basic Python script.

4. Run the program:
    ```bash
    python book_management_system.py
    ```

The program will run in the terminal, displaying a menu for the user to choose operations.

## Usage

Upon running the script, the following menu will appear:

Home book management system

1. Add book


2. Search book


3. Show book information


4. Edit book information


5. Remove book


6. Sign out



Users can select an option by entering the corresponding number. The available actions are:

- **Add book**: Allows the user to enter the title, author, ISBN, release date, and number of copies for a new book.
- **Search book**: Allows the user to search for books by title, author, or ISBN.
- **Show book information**: Displays detailed information about a book when the user provides the ISBN.
- **Edit book information**: Allows the user to modify a book's details (e.g., title, author, ISBN).
- **Remove book**: Removes a book from the collection by its ISBN.
- **Sign out**: Exits the program.

## Functions

### `Add_book()`
Prompts the user to enter details for a new book and adds it to the book list.

### `search_books()`
Allows the user to search for books based on title, author, or ISBN. Displays a list of matching books.

### `show_book_details(book)`
Displays detailed information about a specific book, including title, author, ISBN, release date, and number of copies.

### `edit_book(book)`
Enables the user to edit the details of an existing book.

### `delete_book(book)`
Removes a book from the collection.

