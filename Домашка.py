import os


class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author
    ruName = "Библиотека 1"
    def __str__(self):
        return f'{self.title}, {self.year}, {self.author}'


class Library:
    def __init__(self):
        self.books = []
        

    def add(self, book):
        self.books.append(book)

    def removeAt(self):
        self.books.pop(user_delite)

    def printAll(self):
        print(", ".join(bible_name))
        # print(self.books)
        

    def printAt(self, books):
        print(books[user_info])
            



isWork = True



b = Book("Война и мир", 1990, "Ангелина")
b2 = Book("Я", 1343, "Я")
b3 = Book("Алеша", 1431, "Я")
bible_name = []
bible_name.append(b.title)
bible_name.append(b2.title)
bible_name.append(b3.title)
bible = Library()
bible.add(b)
bible.add(b2)
bible.add(b3)

if __name__ == '__main__':
    while isWork == True:
        print('-------------------------------------------------------------')
        print("Библиотека №1")
        print("Что хотите сделать?")
        print("Посмотреть список книг из " + Book.ruName + "- 'Book list'")
        print("Удалить книгу - 'Delite'")
        print("Узнать информацию об отдельной книге - 'Info book'")
        print("Добавть книгу - 'Add book'")
        print("Выйти - 'Exit'" )
        user = input(">>:")
        if user == "Exit":
            isWork = False
            continue
        if user == "Add book":
            user_title = input('Введите название книги \n')
            user_year = int(input('Введите год создания книги \n'))
            user_author = input('Введите автора книги \n')
            b = Book(user_title, user_year, user_author)
            bible.add(b)
            bible_name.append(b.title)
            continue
        if user == "Book list":
            bible.printAll()
            continue
        if user == "Delite":
            bible.printAll()
            user_delite = int(input('Введите номер книги, которую хотите удалить\n'))
            user_delite = user_delite - 1
            bible.removeAt()
            bible_name.pop(user_delite)
            continue
        if user == "Info book":
            bible.printAll()
            user_info = int(input("Введите номер книги информацию о которой хотите получить\n"))
            user_info = user_info - 1
            continue
        
    print("Good bay")
            
            
            
            
            
             
                    
        
        