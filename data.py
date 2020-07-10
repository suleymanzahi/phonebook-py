class Phonebook:
    def __init__(self, contacts_list):
        self.list = contacts_list

class Contact:
    def __init__(self, first_name, last_name, number):
        self.fname = first_name
        self.lname = last_name
        self.nbr = number
