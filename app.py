
import time
import os
import file_ops as f
from model import *

#helpers
def create_contact():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    num = input("Enter number: ")
    return Contact(fname, lname, num)

def verify_contact(c, name, lname):
     return name in c.fname and lname in c.lname

     
def print_contact(c):
    print(f"Name: {c.fname} {c.lname}")
    print(f"Number: {c.nbr}")

def json_list_add(c,lst):
        lst.append(vars(c))

def not_empty_list(lst):
    return len(lst) != 0


menu = """
Choose one the alternatives below:
1. Add new contact
2. Search for contact
3. Show all contacts
4. Remove a contact
5. Exit application
"""

file_name = 'contacts.txt'
json_file = 'data.json'

empty_list = []
json_list = []
pb = Phonebook(empty_list)
program = True


if not f.file_is_empty(json_file):
    f.load_from_json(json_file, json_list, pb)

print(pb.contacts_list)

    
while program:

   

    print(menu)
    choice = input("Choose option: ")
    if choice == "1":
        c = create_contact()
        pb.contacts_list.append(c)
        print(f'Contact {c.fname} {c.lname} with number {c.nbr} successfully created.')
        json_list_add(c,json_list)
        f.write_to_json(json_file,json_list)
        time.sleep(2)

    elif choice == "2":
        if not_empty_list(pb.contacts_list):
            name = input("Enter first name:")
            lname = input("Enter last name:")
            for c in pb.contacts_list:
                if verify_contact(c, name, lname):
                    print("")
                    print_contact(c)
                    break
            else:
                print("")
                print("No contact found")
        else:
            print("No contacts added yet...")


    elif choice == "3":
        if not_empty_list(pb.contacts_list):
            print("----CONTACTS LIST----------")
            for c in pb.contacts_list:
                print(pb.contacts_list.index(c) + 1)
                print_contact(c)
                print("--------------------")
        else:
            print("No contacts added yet...")


    elif choice == "4":
        if not_empty_list(pb.contacts_list):
            name = input("Enter first name:")
            lname = input("Enter last name:")
            copy = pb.contacts_list
        
            for c in copy:
                if verify_contact(c, name, lname):
                    print(pb.contacts_list.index(c))
                    json_list.pop(pb.contacts_list.index(c))
                    pb.contacts_list.remove(c)
                    f.write_to_json(json_file,json_list)
                    print(f"{c.fname} {c.lname} removed succesfully")
                else:
                    print("No contact found")
        else:
            print("No contacts added yet...")

                    
    elif choice == "5":
        program = False
        print("Exiting application...")
        time.sleep(1)
    else:
        print("Input failed. Try again")

