
import time
import file_ops as f
import data as d 

def create_contact():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    tretto = input("Enter number: ")
    return d.Contact(fname, lname, tretto)



menu = """
Choose one the alternatives below:
1. Add new contact
2. Search for contact
3. Show all contacts
4. Remove a contact
4. Exit application
"""
file_name = 'contacts.txt'
contacts_list = []
program = True

while program:
    
    print(menu)
    choice = input("Choose option: ")
    if choice == "1":
        c = create_contact()
        print(f'Contact {c.fname} {c.lname} with number {c.nbr} successfully created.')
        contacts_list.append(c)
        f.write_to_file(c, file_name)
        time.sleep(2)
    elif choice == "3":
        for c in contacts_list:
            print(contacts_list.index(c) + 1)
            print(f"Name: {c.fname} {c.lname}")
            print(f"Number: {c.nbr}")
            print("--------------------")
    elif choice == "4":
        program = False
        print("Exiting application...")
        time.sleep(1)
    else:
        print("Input failed. Try again")

