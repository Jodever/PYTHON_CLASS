#Library system specifications
# add/view books using classes
# file storage

class Library:
    def __init__(self, book_title:str, book_author:str): #INITIALISES THE LIBRARY CLASS
        self.book_title = book_title
        self.book_author = book_author

    def store(book_title, book_author): #FUNCTION TO STORE THE BOOKS
        cover = book_title +"\nby\n"+ book_author
        with open(cover, mode= 'w', encoding='utf-8') as c:
            c.write(input("Input your content\n"))


    def retrieve(book_title, book_author): #FUNCTION TO RETRIEVE BOOKS IN THE LIBRARY
        cover = book_title +"\nby\n"+ book_author
        with open(cover, mode= 'r', encoding='utf-8') as c:
            print(c.read())

#DIFFERENT DEPARTMENTAL BOOKS IN THE LIBRARY CLASSES(CONCEPT OF INHERITANCE) 
class ASEBooks(Library):
    pass
class CivilBooks(Library):
    pass
class CPEBooks(Library):
    pass
class ECEBooks(Library):
  pass
class MechBooks(Library):
    pass


#functions to add and view books
#add books
def add_books()-> None:
    book_type:int = int(input("What book are you adding to the library today?\n1.ASE\n2.Civil\n3.CPE\n4.ECE\n5.MECH\n"))

    if book_type == 1:
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        ASEBooks.store(title, author)

    elif book_type == 2:
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        CivilBooks.store(title, author)
    
    elif book_type == 3:
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        CPEBooks.store(title, author)

    elif book_type == 4:
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        ECEBooks.store(title, author)

    elif book_type == 5:
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        MechBooks.store(title, author)
    else:
        print("Wrong input.Check again.")

    


#view books
def view_book():
    book_type:int = int(input("What book are you viewing today?\n1.ASE\n2.Civil\n3.CPE\n4.ECE\n5.MECH\n"))

    if book_type == 1:
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        ASEBooks.retrieve(title, author)

    elif book_type == 2:
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        CivilBooks.retrieve(title, author)

    elif book_type == 3:
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        CPEBooks.retrieve(title, author)

    elif book_type == 1:
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        ECEBooks.retrieve(title, author)

    elif book_type == 1:
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        MechBooks.retrieve(title, author)

    else:
        print("Wrong input.Check again.")


while True:
    print("Welcome to our Python Class Library")
    user_action = int(input("Are you adding or viewing a book?\n1.Add\n2.View\n"))

    if user_action == 1:
        add_books()

    elif user_action == 2:
        view_book()

    else:
        print("That's a wrong choice")
