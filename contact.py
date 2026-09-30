def enter_contact():
    print("\n----- Enter Contact Details -----")
    #Get name
    while True:
        name = input("Enter name: ").strip()
        if name == "":
            print("Name cannot be empty. Please enter a valid name.")
        else:
            break
    #Get phone number
    while True:
        phone = input("Enter phone number: ").strip()
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Invalid phone number. Please enter a valid 10-digit phone number.")
    #Get email
    while True:
        email = input("Enter email address: ").strip()
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email address! Please try again.")
            
    contact = {
        "name": name ,
        "phone": phone ,
        "email": email
   }

    return contact
