#I upgrade the code of Shift_ 
#(https://www.daniweb.com/programming/software-development/threads/361480/phonebook-program)

import os

class Phonebook:
    def __init__(self):
        self.phonebook = {}
        self.phonebook_file = 'Phonebook.txt'
    def loadAll(self):
        #Clear the phonebook dictionary
        self.phonebook.clear()
        
        #Load all of the items from the text file into the dictionary
        file = open(self.phonebook_file, 'r')
        for line in file.readlines():
            name, number = line.strip().split()
            self.phonebook[name] = number
        file.close()

    def createFile(self):
        #Check if the file exists on your computer and create the file if it does not exist
        if os.path.exists(self.phonebook_file): 
            print("PHONEBOOK ALREADY EXISTS")
            file = open(self.phonebook_file, 'r')
        else:
            file = open(self.phonebook_file, 'w')
            print("PHONEBOOK CREATED SUCCESSFULLY")
        file.close()
        
    def addEntry(self):
        self.loadAll()
        #Prompt the user for the details of the new entry
        name = input("ENTER NAME: ")
        number =input("ENTER NUMBER: ")
       if not name or number:
            print("EMPTY STRING. NEW CONTACT IS NOT CREATED")
            return
       
        #Создать строку для записи в файл
        new_entry = name + '\t' + number + '\n'
        #Записать строку в файл
        file = open(self.phonebook_file, 'a')
        file.write(new_entry)
        file.close()
        print("NEW CONTACT CREATED SUCCESSFULLY")
        
    def readAll(self):
        self.loadAll()
        #Распечатать весь словарь телефонной книги
        for name, number in self.phonebook.items():
            print(name, " : ", number)
        if len(self.phonebook) == 0:
            print("PHONEBOOK IS EMPTY")
            
    def searchEntry(self):
        self.loadAll()
        #Prompt the user for the name to search for, and search the phonebook dictionary
        search = input("ENTER NAME TO SEARCH FOR: ")
        if search in self.phonebook.keys():
            print(search, " : ", self.phonebook[search])
        else:
            print("ENTRY NOT FOUND")
            
    def deleteEntry(self):
        self.loadAll()
        entry_to_delete = input("ENTER NAME OF ENTRY TO DELETE: ")
        if entry_to_delete in self.phonebook.keys():
            del self.phonebook[entry_to_delete]
            file = open(self.phonebook_file, 'w')
            for name, number in self.phonebook.items():
                string = name + '\t' + number + '\n'
                file.write(string)
            file.close()
            print("ENTRY DELETED SUCCESSFULLY")
        else:
            print("ENTRY NOT FOUND")
    def exitProgram(self):
        os._exit
    def menu(self):
        print("""\
       -МЕНЮ-
1) READ ALL ENTRIES
2) ADD AN ENTRY
3) DELETE AN ENTRY
4) LOOK UP AN ENTRY
5) Exit\n""")
        choice = input("ENTER CHOICE: ")
        choice_menu = {'1' : self.readAll,
                       '2' : self.addEntry,
                       '3' : self.deleteEntry,
                       '4' : self.searchEntry,
                       '5' : self.exitProgram}
        if choice not in choice_menu.keys():
            print("PLEASE ENTER A VALID CHOICE")
        else:
            choice_menu[choice]()
            
Book_1 = Phonebook()
Book_1.menu()