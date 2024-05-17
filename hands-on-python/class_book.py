# Create a class called Book that has attributes title, author, and publication_year.
# Add a method get_age that calculates how many years ago the book was published.

# Create a class called Book that has attributes title, author, and publication_year.
from datetime import date
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    # Add a method get_age that calculates how many years ago the book was published using the current year as default,
    # or a specific year as argument and return the subtraction of the current year and the publication year.
    def get_age(self, year=date.today().year):
        return year - self.publication_year

# Create an instance of the Book class with a title, author and publication year as arguments
book = Book("Understanding Algorithms", "Aditya Y. Bhargava", 2015)
# print the book instance with the title, how many years ago the book was published and the publication year
print(f"The book '{book.title}' was published {book.get_age()} years ago in {book.publication_year}.")


