from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display():
        pass


class MyBook(Book):
    def __init__(self, price, title, author):
        self.price = price
        super().__init__(title, author)

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


title = input("Enter the title of the book: ")
author = input("Author: ")
price = int(input("Price: "))

b1 = MyBook(price, title, author)
b1.display()
