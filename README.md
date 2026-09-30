📒 Contact Book Application

A simple command-line contact book built with Python. You can add, view, search, edit and delete contacts, and everything is saved to a text file, so your contacts are still there the next time you open the program.

I made this as my Python Essentials project in my first semester. The goal was to put functions, file handling and input validation into something that actually works and is useful.

What it does
Add a new contact (name, phone number, email)
View all saved contacts
Search for a contact by name
Modify an existing contact
Delete a contact
Check the phone number and email before saving
Stop you from saving the same phone number twice
Save contacts to a text file and load them again when the program starts
Why I built it
To make a simple contact management app from scratch
To practise using Python functions and file handling in a real project
To add search, edit and delete options, not just "add" and "view"
To keep data saved permanently instead of losing it when the program closes
Built with
Python
Visual Studio Code
A plain text file (contacts.txt) for storage
Project structure
Contact_Book/
│
├── main.py
├── contact.py
├── contact_operations.py
├── contacts.txt
└── README.md
File	What it does
main.py	The starting point. Shows the menu and connects everything together.
contact.py	Handles typing in the details of a new contact (name, phone, email).
contact_operations.py	The main logic: add, view, search, modify and delete contacts, plus saving to and loading from the file.
contacts.txt	Where the contacts are stored so they don't disappear when you close the program.
How to run it
Make sure Python is installed on your computer.
Open the project folder in Visual Studio Code.
Check that all the project files are in the same folder.
Open main.py.
Run it using the Run button in VS Code, or from the terminal:
python main.py

You'll see this menu:

=========================================
        CONTACT BOOK APPLICATION
=========================================
1. Add Contact
2. View All Contacts
3. Search Contact
4. Modify Contact
5. Delete Contact
6. Exit
=========================================

Type the number of the option you want and follow the instructions on screen.

How contacts are stored

Each contact has a name, a phone number and an email address.

They are saved in contacts.txt. The file is updated whenever you add, modify or delete a contact, and the saved contacts are loaded automatically when the program starts.

Input checks

The program checks what you type before saving it:

The name can't be empty
The phone number must be exactly 10 digits
The email must contain @ and .
A phone number that already exists can't be added again
