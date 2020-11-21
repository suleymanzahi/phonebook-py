
import json
from model import *
import os

def write_to_json(file, lst):
    with open(file, 'w') as f:
        json.dump(lst,f, indent = 2)


def load_from_json(file, lst, phonebook):
    with open(file, 'r') as f:
        json_array = json.load(f)
        for contact in json_array:
            c = Contact(contact['fname'], contact['lname'], contact['nbr'] )
            phonebook.contacts_list.append(c)
            lst.append(vars(c))


def file_is_empty(path):
    return os.stat(path).st_size==0
