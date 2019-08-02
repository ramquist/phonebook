# I upgrade the code of Shift_ 
# (https://www.daniweb.com/programming/software-development/threads/361480/phonebook-program)

import os
import re

class Phonebook:
    def __init__(self): 
        self.phonebook = {}
        print("WELCOME TO THE PROGRAM 'THE PHONEBOOK'")
        # Prompt name of file
        self.open_file()

    def load_all(self):
        # Clear the phonebook dictionary
        self.phonebook.clear()
        
        # Load all of the items from the text file into the dictionary
        file = open(self.phonebook_file, 'r')
        for line in file.readlines():
            name, number = line.strip().split()
            self.phonebook[name] = number
        file.close()

    def open_file(self):
        # Check if the file exists on your computer and create the file if it does not exist
        file_name = input("ENTER THE FILE NAME WITHOUT THE EXTENSION: ")
        self.phonebook_file = file_name + '.txt'
        if os.path.exists(self.phonebook_file): 
            print("PHONEBOOK ALREADY EXISTS AND IS OPEN")
            return
        else:
            file = open(self.phonebook_file, 'w')
            print("PHONEBOOK CREATED SUCCESSFULLY")
        
    def add_contact(self):
        self.load_all()
        # Prompt the user for the details of the new entry
        name = input("ENTER NAME: ")
        if name == "":
            print("EMPTY STRING. NEW CONTACT IS NOT CREATED")
            return
        number =input("ENTER NUMBER: ")
        if number == "":
            print("EMPTY STRING. NEW CONTACT IS NOT CREATED")
            return
        if name in self.phonebook.keys():
            change_name = input("CONTACT ALREADY EXISTS. DO YOU WANT TO CHANGE IT? ENTER 'YES' or 'NO': ")
            if change_name == "NO" or "no":
                print("CONTACT WILL NOT BE OVERWRITTEN")
                return
            elif change_name == "YES" or "yes":
                print("OK. CONTACT WILL BE OVERWRITTEN")

        # Create a string to be written to the file
        new_contact = name + '\t' + number + '\n'
        # Write the string to the file
        file = open(self.phonebook_file, 'a')
        file.write(new_contact)
        file.close()
        print("NEW CONTACT CREATED SUCCESSFULLY")
        
    def read_all(self):
        self.load_all()
        # Print out the entire phonebook dictionary
        list_keys = list(self.phonebook.keys())
        # Converting a dictionary to a list, sorting the list alphabetically
        list_keys.sort()
        for i in list_keys:
            print(i, ':', self.phonebook[i])
        if len(self.phonebook) == 0:
            print("PHONEBOOK IS EMPTY")
            
    def search_name(self):
        self.load_all()
        # Prompt the user for the name to search for, and search the phonebook dictionary 
        pattern = input("ENTER CONTACT NAME: ").strip()
        occurrences = 0
        for name, number in self.phonebook.items():
            # Use regex for partial search
            if re.search(pattern, name):
                occurrences += 1
                print(name, ':', number)
        if occurrences == 0:
                print("CONTACT NOT FOUND")

    def search_number(self):
        self.load_all()
        # Prompt the user for the number to search for, and search the phonebook dictionary 
        pattern = input("ENTER CONTACT NUMBER: ").strip()
        occurrences = 0
        for name, number in self.phonebook.items():
            # Use regex for partial search
            if re.search(pattern, number):
                occurrences += 1
                print(name, " : ", number)
        if occurrences == 0:
            print("CONTACT NOT FOUND")

    def delete_contact(self):
        self.load_all()
        contact_to_delete = input("ENTER NAME OF CONTACT TO DELETE: ")
        if contact_to_delete in self.phonebook.keys():
            del self.phonebook[contact_to_delete]
            file = open(self.phonebook_file, 'w')
            for name, number in self.phonebook.items():
                string = name + '\t' + number + '\n'
                file.write(string)
            file.close()
            print("CONTACT DELETED SUCCESSFULLY")
        else:
            print("CONTACT NOT FOUND")

    def exit_program(self):
        os._exit

    def menu(self):
        while True:
            print("""\
       -МЕНЮ-
1) OPEN THE PHONEBOOK
2) READ ALL CONTACTS
3) ADD AN CONTACT
4) DELETE AN CONTACT
5) SEARCH CONTACT BY NAME
6) SEARCH CONTACT BY NUMBER
7) EXIT\n""")
            choice = input("ENTER CHOICE: ")
            choice_menu = {'1' : self.open_file,
                           '2' : self.read_all,
                           '3' : self.add_contact,
                           '4' : self.delete_contact,
                           '5' : self.search_name,
                           '6' : self.search_number,
                           '7' : self.exit_program}
            if choice not in choice_menu.keys():
                print("PLEASE ENTER A VALID CHOICE")
            elif choice == '7':
                break
            else:
                choice_menu[choice]()
            
Book_1 = Phonebook()
Book_1.menu()
