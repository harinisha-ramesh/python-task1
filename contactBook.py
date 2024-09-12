contacts = {}

def add_contact():
    name = input("Enter the contact name: ").strip()
    phoneNumber = input("Enter the contact number: ").strip()
    contacts[name] = phoneNumber
    print(f"Contact {name} Added Successfully.")

def remove_contact():
    name = input("Enter the contact name to remove: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} Deleted Successfully")
    else:
        print(f"Contact {name} not found")

def lookup_contact():
    name = input("Enter the contact name to have a look: ").strip()
    phoneNumber = contacts.get(name)
    if phoneNumber:
        print(f"Contact {name} has phone Number: {phoneNumber} ")
    else:
        print(f"Contact {name} not found")    

def display_contacts():
    if contacts:
        print("ALL CONTACTS:")
        for name,phoneNumber in contacts.items():
            print(f"Contact name: {name} , Phone Number: {phoneNumber}")
    else:
        print("No Contacts Available")        

def application():
    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Look up  Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            remove_contact()
        elif choice == '3':
            lookup_contact()
        elif choice == '4' :
            display_contacts()
        elif choice == '5':
            print("Exiting the Contact Book Application,Thank you!")
            break    
        else:
            print("Please choose the option between 1 to 5.")

if __name__ == "__main__":
    application()         
           