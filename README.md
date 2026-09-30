Contact Book Application
Introduction

The Contact Book Application is a simple Python-based project used to store and manage contact information. It allows the user to add, view, search, modify, and delete contacts.

The application stores the contact's name, phone number, and email address. The contacts are saved in a text file so that the data can be accessed again when the program is run.

Objectives
To create a simple contact management application.
To store contact names, phone numbers, and email addresses.
To provide options for searching, modifying, and deleting contacts.
To use Python functions and file handling in a practical project.
To provide permanent storage for the saved contacts.
Features
Add a new contact
View all saved contacts
Search for a contact by name
Modify existing contact details
Delete a contact
Check phone number and email input
Prevent duplicate phone numbers
Save contacts in a text file
Load saved contacts when the application starts
Technologies Used
Python
Visual Studio Code
Text file for data storage
Project Structure
Contact_Book/
│
├── main.py
├── contact.py
├── contact_operations.py
├── contacts.txt
└── README.md
main.py

This is the main module of the application. It displays the menu and connects the different operations of the Contact Book.

contact.py

This module is used to enter the details of a new contact, including name, phone number, and email address.

contact_operations.py

This module contains the main operations such as adding, viewing, searching, modifying, and deleting contacts. It also contains the functions used for saving and loading contacts.

contacts.txt

This file is used to store the contact information so that contacts are not lost after closing the application.

How to Run
Install Python on the computer.
Open the project folder in Visual Studio Code.
Make sure all project files are present in the same folder.
Open main.py.
Run the program using the Python Run option or the terminal.

The program will display the main menu:

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

Enter the number of the required option and follow the instructions shown by the program.

Contact Information

Each contact contains:

Name
Phone Number
Email Address
Data Storage

The application uses a text file named contacts.txt for storing contact information.

The data is saved when a contact is added, modified, or deleted. When the program starts, the saved contacts are loaded from the file.

Input Validation

The application checks the entered information before saving it.

For example:

Name cannot be empty.
Phone number must contain 10 digits.
Email address must contain @ and ..

The application also checks whether a phone number is already present before adding a new contact.

Future Improvements

The project can be improved in the future by adding:

A graphical user interface
A database for storing contacts
Contact sorting
Search by phone number or email
Contact groups
A password or login system
Conclusion

The Contact Book Application provides a simple way to manage contact information using Python. The project demonstrates basic Python programming concepts such as functions, lists, dictionaries, loops, conditional statements, input validation, and file handling.
