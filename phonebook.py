# I upgrade the code of Shift_ 
# (https://www.daniweb.com/programming/software-development/threads/361480/phonebook-program)

import os

class Phonebook:
    def __init__(self): 
        self.phonebook = {}
        # Prompt name of file
        file_name = input("""\
WELCOME TO THE PROGRAM 'THE PHONEBOOK'.
NOW OPEN AN EXISTING BOOK OR CREATE A NEW ONE.
ENTER THE FILE NAME WITHOUT THE EXTENSION: """)
        self.phonebook_file = file_name + '.txt'
        if os.path.exists(self.phonebook_file): 
            print("PHONEBOOK ALREADY EXISTS")
            return
        else:
            file = open(self.phonebook_file, 'w')
            print("PHONEBOOK CREATED SUCCESSFULLY")

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
        number =input("ENTER NUMBER: ")
        if (name == "" or number == ""):
            print("EMPTY STRING. NEW CONTACT IS NOT CREATED")
            return
        if name in self.phonebook.keys():
            print("CONTACT ALREADY EXISTS AND WILL BE REWRITTEN")
        # Create a string to be written to the file
        new_entry = name + '\t' + number + '\n'
        # Write the string to the file
        file = open(self.phonebook_file, 'a')
        file.write(new_entry)
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
            
    def search_contact(self):
        self.load_all()
        # Prompt the user for the name to search for, and search the phonebook dictionary
        search = input("ENTER NAME TO SEARCH FOR: ")
        if search in self.phonebook.keys():
            print(search, " : ", self.phonebook[search])
        else:
            print("CONTACT NOT FOUND")
            
    def delete_contact(self):
        self.load_all()
        entry_to_delete = input("ENTER NAME OF CONTACT TO DELETE: ")
        if entry_to_delete in self.phonebook.keys():
            del self.phonebook[entry_to_delete]
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
5) LOOK UP AN CONTACT
6) EXIT\n""")
            choice = input("ENTER CHOICE: ")
            choice_menu = {'1' : self.open_file,
                           '2' : self.read_all,
                           '3' : self.add_contact,
                           '4' : self.delete_contact,
                           '5' : self.search_contact,
                           '6' : self.exit_program}
            if choice not in choice_menu.keys():
                print("PLEASE ENTER A VALID CHOICE")
            elif choice == '6':
                break
            else:
                choice_menu[choice]()
            
Book_1 = Phonebook()
Book_1.menu()