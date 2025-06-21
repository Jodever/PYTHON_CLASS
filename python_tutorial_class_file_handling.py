#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 14:03:05 2025

@author: jotroniks
"""
#
# f = open('textfile1', mode = 'a')
# write = f.write('new text file contents\n')

# f = open('textfile1', mode = 'r')

# write = f.read()

# with open('textfile', mode = 'a', encoding = "utf-8") as f:
#     write_data = f.write('file with text\n')
    #read_data = f.read()
    
    
    
#-----Basic note taking app-----#
#Should be able to;
#write new files
#read these files
#edit existing files
#exit

#BASIC NOTES APP IN TERMINAL#

#function to write new files
def write():
        name = input("Filename please \n")
        W_content = open(name, mode = 'w', encoding='utf-8')
        W_content.write(input('write your content\n')+ '\n')  
        W_content.close()  
        return print("Created")


#function to read these files
def read():
    name = input("Filename please \n")
    r_content = open(name, mode = 'r', encoding='utf-8')
    print(r_content.read())
    r_content.close()  
    return 0


#function to edit existing files
def edit():
    name = input("Filename please \n")
    W_content = open(name, mode = 'a', encoding='utf-8')
    W_content.write(input('Edit your file \n') + '\n')
    W_content.close()  
    return print("Changes saved")
    

#get the users action
user_input = input("What action are you taking?\n1.Write\n2.Read\n3.Edit\n").lower()

while True:#Ensures the program never stops
    if user_input == "write":
        write() 
    elif user_input == "read":
         read()
    elif user_input == "edit":
        edit()
    else:
        print("Not a valid response")
#various conditions available to the user
 












   
    # from tkinter import *
    # from tkinter import ttk
    # root = Tk()
    # frm = ttk.Frame(root, padding=10)
    # frm.grid()
    # ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    # root.mainloop()


