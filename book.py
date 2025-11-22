import itertools

class Book:
    # Use itertools.count() automatically incrementing counter
    id_iter = itertools.count(start=100000001) # Start IDs from 100000001

    def __init__(self, title, author, genre, availability=None):
        self.book_id = next(Book.id_iter)
        self.title = title
        self.author = author
        self.genre = genre
        if availability is None:
            self.availability = "Available"
        else:
            self.availability = availability

    def __repr__(self):
        return f"Book(ID: {self.book_id}, Title: '{self.title}', Author: '{self.author}' Genre: '{self.genre}', Availability: '{self.availability}')"

# Example usage
#book1 = Book("Python Basics", "Real P.", "Programming")
#book2 = Book("Breaking the Rules", "Stephen G.", "Personal Development")

#print(book1)
#print(book2)

