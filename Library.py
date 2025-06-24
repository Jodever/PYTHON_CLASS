#Library system specifications
# add/view books using classes
# file storage
import os
try:
    os.mkdir('Library')
    os.chdir('Library')
    departments = ['ASE', 'CIVIL', 'CPE', 'ECE', 'SYSTEMS', 'MECH']
    for i in departments:
        os.mkdir(i)
except FileExistsError:
    os.chdir('Library')
    root_dir = os.getcwd()

class Library:
    def __init__(self, book_title:str, book_author:str): #INITIALISES THE LIBRARY CLASS
        self.book_title = book_title
        self.book_author = book_author

    def store(book_title, book_author): #FUNCTION TO STORE THE BOOKS
        cover = f'{book_title} by {book_author}'
        with open(cover, mode= 'w', encoding='utf-8') as c:
            c.write(input("Input your content\n"))


    def retrieve(book_title, book_author): #FUNCTION TO RETRIEVE BOOKS IN THE LIBRARY
        cover = f'{book_title} by {book_author}'
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
class SystemsBooks(Library):
    pass



#functions to add and view books
#add books
def add_books()-> None:
    book_type:int = int(input("What book are you adding to the library today?\n1.ASE\n2.CIVIL\n3.CPE\n4.ECE\n5.MECH\n6.Systems\n"))

    if book_type == 1:
        os.chdir('ASE')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        ASEBooks.store(title, author)

    elif book_type == 2:
        os.chdir('CIVIL')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        CivilBooks.store(title, author)
    
    elif book_type == 3:
        os.chdir('CPE')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        CPEBooks.store(title, author)

    elif book_type == 4:
        os.chdir('ECE')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        ECEBooks.store(title, author)

    elif book_type == 5:
        os.chdir('MECH')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        MechBooks.store(title, author)

    elif book_type == 6:
        os.chdir('SYSTEMS')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        SystemsBooks.store(title, author)

    else:
        print("Wrong input.Check again.")


    


#view books
def read_book():
    book_type:int = int(input("What book are you viewing today?\n1.ASE\n2.Civil\n3.CPE\n4.ECE\n5.MECH\n6.Systems\n"))

    if book_type == 1:
        os.chdir('ASE')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        ASEBooks.retrieve(title, author)

    elif book_type == 2:
        os.chdir('CIVIL')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        CivilBooks.retrieve(title, author)

    elif book_type == 3:
        os.chdir('CPE')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        CPEBooks.retrieve(title, author)

    elif book_type == 4:
        os.chdir('ECE')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        ECEBooks.retrieve(title, author)

    elif book_type == 5:
        os.chdir('MECH')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        MechBooks.retrieve(title, author)

    elif book_type == 6:
        os.chdir('SYSTEMS')
        title = input("What is the book's title?\n")
        author = input("Who is the book's author?\n")
        SystemsBooks.retrieve(title, author)

    else:
        print("Wrong input.Check again.")
        





while True:
    print("\nWelcome to our Python Class Library")
    user_action = int(input("Are you adding or reading a book?\n1.Add\n2.Read\n"))
    
    
    if user_action == 1:
        add_books()
        os.chdir(root_dir)

    elif user_action == 2: 
        read_book()
        os.chdir(root_dir)

    else:
        print("That's a wrong choice")


 
    
