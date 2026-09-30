from contact import enter_contact

from contact_operations import(
    add_contact,
    view_contacts,
    search_contact,
    modify_contact,
    delete_contact,
    load_contacts

)
# Load contacts when the program starts
contacts = load_contacts()


while True:
    print("\n=========================================")
    print("      CONTACT BOOK APPLICATION")
    print("=========================================")
    print("1.Add Contact")
    print("2.View All Contacts")
    print("3.Search Contact")
    print("4.Modify Contact")
    print("5.Delete Contact")
    print("6.Exit")
    print("=============================")
    choice = input("Enter your choice: ")
    if choice=="1":
        contact = enter_contact()
        add_contact(contacts, contact)
    elif choice=="2":
        view_contacts(contacts)
    elif choice=="3":
        search_contact(contacts)
    elif choice=="4":
        modify_contact(contacts)
    elif choice=="5":
        delete_contact(contacts)
    elif choice=="6":
        print("\nThank You for using Contact Book!")
        break
    else:
        print("\nInvalid choice! Please try again.")