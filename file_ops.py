
def write_to_file(contact, contacts_file):
    file = open(contacts_file,"a")
    file.write(f"{contact.fname},{contact.lname},{contact.nbr}")
    file.write('\n')
    file.close()

def create_from_file(file):