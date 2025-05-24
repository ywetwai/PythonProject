class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


    def __str__(self):
        return f"{self.title} by {self.author} (ISBN :{self.isbn})"
    

class Library:
    def __init__(self):
        self.books = []

    def addBook(self,book):
        self.books.append(book)
        print(f"{book} is successfully added")

    def showBook(self):
        if not self.books:
            print("Not in Books")
            return
        print("Library Collection:")
        for x in self.books:
            print(x)
        print()


    def removeBook(self,title):
        removed = False
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Removed")
                removed = True
                return
            
        print("This book is not found in library")

    def searchBook(self, title):
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Book Found")
                print(book)
                found = True
                break
        if not found:
            print("Not found!!")
def main():
    library = Library()
    while True:
        print("1. Add Books")
        print("2. Show Books")
        print("3. Search Books")
        print("4. Remove Books")
        print("5.Exit")
        try:
            choice = int(input("Enter the number (1-5)"))
            if choice == 1:
                title = input("Enter the title")
                author = input("Enter the author name")
                isbn = input ("Enter the isbn number")

                book = Book(title,author,isbn)
                library.addBook(book)

            elif choice == 2:
                library.showBook()

            elif choice == 3:
                title = input ("Enter the title ")
                library.searchBook(title)
            elif choice == 4:
                title = input("Enter the title")  
                library.removeBook(title)

            else:
                print("Bye")
                break
        except ValueError:
            print("Invlid value")

if __name__ == "__main__":
    main() 


