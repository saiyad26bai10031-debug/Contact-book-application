def add_contact(contacts, contact):
    #Check for duplicate phone number
    for existing_contact in contacts:
        if existing_contact['phone'] == contact['phone']:
            print("\nA contact with this phone number already exists. Contact not added.")
            return
    contacts.append(contact)
    save_contacts(contacts)
    print("\nContact added successfully!")
def view_contacts(contacts):
    if len(contacts) == 0:
        print("\nNo contacts found.")
        return
    print("\n=========================================")
    print("\n        Contact List")
    print("==========================================")
    for i, contact in enumerate(contacts, start=1):
        print(f"\ncontact {i}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}") 
        print(f"Email: {contact['email']}")

        print("\n=========================================")
def search_contact(contacts):
    name = input("\nEnter name to search: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("\nContact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return
    print("\nContact not found.")
def modify_contact(contacts):
    name = input("\nEnter name of the contact to modify: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("\nEnter new details:")
            #New name
            while True:
                new_name = input("Enter new name: ").strip()
                if new_name == "":
                    print("Name cannot be empty. Please enter a valid name.")
                else:
                    contact['name'] = new_name
                    break
            #New phone 
            while True:
                new_phone = input("Enter new phone number: ").strip()
                if new_phone.isdigit() and len(new_phone) == 10:
                    contact['phone'] = new_phone
                    break
                else:
                    print("Invalid phone number. Please enter a valid 10-digit phone number.")
            #New email
            while True:
                new_email = input("Enter new email address: ").strip()
                if "@" in new_email and "." in new_email:
                    contact['email'] = new_email
                    break
                else:
                    print("Invalid email address! Please try again.")
            contact['name'] = input("Enter Name: ")
            contact['phone'] = input("Enter Phone Number: ")
            contact['email'] = input("Enter Email Address: ")
            save_contacts(contacts)
            print("\nContact modified successfully!")
            return
    print("\nContact not found.")
def delete_contact(contacts):
    name = input("\nEnter name of the contact to delete: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("\nContact found!" )
            print("Name :", contact["name"])
            print("Phone :", contact["phone"])
            print("Email :", contact["email"])
            confirmation = input("Are you sure you want to delete this contact? (y/n): ").strip().lower()
            if confirmation == "y":
                contacts.remove(contact)
                save_contacts(contacts)
                print("\nContact deleted successfully!")
            else:
                print("\nDeletion cancelled.")
            return
    print("\nContact not found.")   

def save_contacts(contacts):
    file = open("contacts.txt", "w")
    for contact in contacts:
        file.write(
            contact["name"]+ "|"+
            contact["phone"]+ "|"+
            contact["email"]+ "\n"  
        )
        file.close() 
def load_contacts():
    contacts = []


    try:
        file = open("contacts.txt", "r")

        for line in file:
            data = line.strip().split("|")

            if len(data) == 3:
                contact = {
                    "name": data[0],
                    "phone": data[1],
                    "email": data[2]
                }

                contacts.append(contact)

        file.close()

    except FileNotFoundError:
        pass

    return contacts       
