#writing files
# f_w = open('textfile2', mode = 'w', encoding = 'utf-8')
# f_w.write('This is a new textfile for practice')
# f_w.close()

# #readiing files
# f = open('textfile2', mode = 'r', encoding = 'utf-8')
# print(f.read())
# f.close()

# f = open('textfile2', mode = 'r', encoding = 'utf-8')
# for line in f: print(line, end = ('\n'))
# f.close()

#adding text to an exissting file
# f = open('textfile2', mode = 'a', encoding = 'utf-8')
# f.write('\nNow I am adding new text to this document')
# f.close()




# with open('textfile', mode = 'w', encoding = "utf-8") as f:
#     write_data = f.write("testing the with keyword")

# with open('textfile', mode = 'r', encoding = "utf-8") as f:
#     write_data = f.read()

# with open('textfile', mode = 'a', encoding = "utf-8") as f:
#     write_data = f.append()


# basic notes app
#Should be able to;
#write new files
#read these files
#edit existing files
#exit

#BASIC NOTES APP IN TERMINAL#
#write new files
# def write():
#         name = input("Filename please\n")
#         W_content = open(name, mode = 'w', encoding='utf-8')
#         W_content.write(input('write your content\n')+ '\n')  
#         W_content.close()  
#         return print("Created\n")

#def write():
        # name = input("Filename please\n")
        # with open(name, mode = 'w', encoding='utf-8') as name:
        #         name.write(input('write your content\n')+ '\n')
        #         return print("Created\n")

#read/open these files
# def read():
#         name = input("Filename please\n")
#         r_content = open(name, mode = 'r', encoding='utf-8')
#         print(r_content.read())
#         r_content.close()  
        

#def read() -> str:
        # name = input("Filename please\n")
        # with open(name, mode = 'r', encoding='utf-8') as name:
        #         a = print(name.read())
        #         return a
          


#edit existing files
# def edit():
#         name = input("Filename please\n")
#         W_content = open(name, mode = 'a', encoding='utf-8')
#         W_content.write(input('Edit your file \n') + '\n')
#         W_content.close()  
#         return print("Changes saved\n")


#def edit():
        # name = input("Filename please\n")
        # with open(name, mode = 'a', encoding='utf-8') as name:
        #         name.write(input('Edit your file \n') + '\n')
        #         return print("Changes saved\n")



#while True:
        # user_input = input("What action are you taking?\n1.Write\n2.Read\n3.Edit\n") #takes in a string(read, write or edit)
        # user_input = user_input.lower()

        # if user_input == "write":
        #         write()
        # elif user_input == "read":
        #         read()
        # elif user_input == "edit":
        #         edit()
        # else:
        #         print("Not a valid response")


