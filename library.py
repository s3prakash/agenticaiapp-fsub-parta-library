# Book Record Management System
import csv
from book import Book

class Library:

    books = []  # List to store book records

    def load_books_from_csv(self, filename):
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    book = Book(
                        row["Title"],
                        row["Author"],
                        row["Genre"],
                        row["Availability"]
                    )
                    self.books.append(book)

            print(f"Loaded {len(self.books)} books from {filename}.\n")

        except FileNotFoundError:
            print(f"CSV file '{filename}' not found. Starting with an empty library.\n")

    def add_book(self):
        print("\n--- Add New Book ---")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        genre = input("Enter Genre: ")

        book = Book(title, author, genre)
        self.books.append(book)
        print("Book added successfully!\n")

    def view_books(self):
        print("\n--- Book Records ---")
        if not self.books:
            print("No records found.\n")
            return

        for i, book in enumerate(self.books, 1):
            print(f"Record {i}:")
            print(book)
            print()

    def search_book_by_author(self, author):
        if not self.books:
            print("No records found.\n")
            return

        for i, book in enumerate(self.books, 1):
           if book.author == author:
                print("Book Found")
                #print(book)
                return book
        return

    def search_book_by_title(self, title):
        if not self.books:
            print("No records found.\n")
            return

        for i, book in enumerate(self.books, 1):
            if book.title == title:
                print("Book Found")
                #print(book)
                return book
        return

    def borrow_book(self):
        #check if book is present in the books list
    
        while True:
            searchby = input("\n--- Search Book by Author(a) or Title(t)---")
            if searchby == 'a':
                author = input("Enter Author: ")
                book = self.search_book_by_author(author)
                print(book)
            elif searchby == 't':
                title = input("Enter Title: ")
                book = self.search_book_by_title(title)
            elif searchby == 'q':
                break
            else:
                print("Enter 'a' for Author Search or t for title search or q for Quit")
                continue
            if book:
                if book.availability == 'Available':
                    book.availability = "Issued"
                    print("Book borrowed successfully")
                else:
                    print("Book already borrowed. Hence cannot be issued")
                break
            else:
                print("Book not found")
                break

    def return_book(self):
        #check if book is present in the books list
    
        while True:
            searchby = input("\n--- Search Book by Author(a) or Title(t) or Quit(q)---")
            if searchby == 'a':
                author = input("Enter Author: ")
                book = self.search_book_by_author(author)
                print(book)
            elif searchby == 't':
                title = input("Enter Title: ")
                book = self.search_book_by_title(title)
            elif searchby == 'q':
                break
            else:
                print("Enter 'a' for Author Search or t for title search or q for Quit")
                continue
            if book:
                if book.availability == 'Issued':
                    book.availability = "Available"
                    print("Book returned successfully")
                else:
                    print("Book already in Returned status. Hence cannot be returned")
                break
            else:
                print("Book not found")
                break
