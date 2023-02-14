contacts = {}


def main():
    # Ask the user for an option
    while True:
        print("""
              Press 1 for Adding Contact
              Press 2 to view contact
              Press 3 to search contact
              Press 4 to Remove contact
              Press 5 to exit the Program
              """)

        resp = input("Please select an option: ")
        # checks the user response
        if resp == "1":
            add_con()
            continue
        elif resp == "2":
            view_con()
            continue
        elif resp == "3":
            search_con()
            continue
        elif resp == "4":
            rem_con()
            continue
        elif resp == '5':
            break
        else:
            print("you have not made a valid choice")
            continue

# adds contact to the phone book


def add_con():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter an Email")
    contacts[name] = {'name': name, 'phone': phone, 'email': email}
    print(contacts[name])

# view contacts in the phone book


def view_con():
    for name, info in contacts.items():
        print("Name", name)
        print("Phone", info['phone'])
        print("Email", info['email'])

# search contacts in the phone book


def search_con():
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print("Name", info['name'])
        print("Phone", info['phone'])
        print("Email", info['email'])
    else:
        print("Contact not found")

# remove contacts from the phone book


def rem_con():
    name = input("Enter contact to remove: ")
    if name in contacts:
        del contacts[name]
        print("contact removed successfully")
    else:
        print("contact not found")


main()
