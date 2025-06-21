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


# w = writing
# r = reading the text File
# a = append or edit a text file

#editing or appending contents to existing files
a = open("new_file", mode = 'a', encoding= 'utf-8')
a.write("\nAppending a new line of text")
a.close()

# a = open("pythonClassFile1", mode = 'w', encoding= 'utf-8')
# a.write("\nAppending a new line of text")
# a.close()



with open("pythonClassFile1", mode = 'w', encoding= 'utf-8') as t:
    t.write("Testing the with keyword")