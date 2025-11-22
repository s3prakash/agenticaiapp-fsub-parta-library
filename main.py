# main.py
from library import Library

def main():
    library = Library()
    while True:
        print("========== Book Record Management ==========")
        print("0. Add Books from CSV file")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Borrow A Book")
        print("4. Return A Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "0":
            library.load_books_from_csv("books.csv")
        elif choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run program
if __name__ == "__main__":
    main()
