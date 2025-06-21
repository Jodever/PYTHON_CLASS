# w = writing
# r = reading the text File
# a = append or edit a text file

#open() and write() files

f = open("new_file", mode = 'w', encoding= 'utf-8')
write_to_f = f.write("Reading and writing text files in python")
f.close()

n = open("pythonClassFile1", mode= 'w', encoding= 'utf-8')
n.write("This is a new python class file")
n.close()


#read()
w = open("new_file", mode = 'r', encoding= 'utf-8')
read_from_w = print(w.read())
w.close()

w = open("pythonClassFile1", mode = 'r', encoding= 'utf-8')
read_from_w = print(w.read())
w.close()

#editing or appending contents to existing files
a = open("new_file", mode = 'a', encoding= 'utf-8')
a.write("\nAppending a new line of text")
a.close()

# a = open("pythonClassFile1", mode = 'w', encoding= 'utf-8')
# a.write("\nAppending a new line of text")
# a.close()


#applying the with keyword
with open("pythonClassFile1", mode = 'w', encoding= 'utf-8') as t:
    t.write("Testing the with keyword")






# basic notes app
#Should be able to;
#write new files
#read these files
#edit existing files
#exit

#BASIC NOTES APP IN TERMINAL#
#write new files
def write():
        name = input("Filename please\n")
        W_content = open(name, mode = 'w', encoding='utf-8')
        W_content.write(input('write your content\n')+ '\n')  
        W_content.close()  
        return print("Created\n")


#read/open these files
def read():
        name = input("Filename please\n")
        r_content = open(name, mode = 'r', encoding='utf-8')
        print(r_content.read())
        r_content.close()  



#edit existing files
def edit():
        name = input("Filename please\n")
        W_content = open(name, mode = 'a', encoding='utf-8')
        W_content.write(input('Edit your file \n') + '\n')
        W_content.close()  
        return print("Changes saved\n")


while True:
        user_input = input("What action are you taking?\n1.Write\n2.Read\n3.Edit\n") #takes in a string(read, write or edit)
        user_input = user_input.lower()

        if user_input == "write":
                write()
        elif user_input == "read":
                read()
        elif user_input == "edit":
                edit()
        else:
                print("Not a valid response")
