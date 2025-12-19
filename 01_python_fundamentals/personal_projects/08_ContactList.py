# -------------------------------------------------
# Contact List Manager
# -------------------------------------------------
# This program allows the user to add, view,
# search, and delete contacts using a simple
# text-based menu.
# -------------------------------------------------

contacts = []  # List to store contact dictionaries

while True:
    # Display menu options
    print("\nContact List Menu")
    print("1 - Add Contact")
    print("2 - View All Contacts")
    print("3 - Search Contact")
    print("4 - Delete Contact")
    print("5 - Quit")

    choice = input("Enter your choice: ")

    # Add a new contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added successfully.")

    # View all contacts
    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nSaved Contacts")
            print("-" * 30)
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

    # Search for a contact by name
    elif choice == "3":
        search_name = input("Enter name to search: ").lower()
        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name:
                print("\nContact Found")
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete a contact
    elif choice == "4":
        delete_name = input("Enter name to delete: ").lower()
        for contact in contacts:
            if contact["name"].lower() == delete_name:
                contacts.remove(contact)
                print("Contact deleted.")
                break
        else:
            print("Contact not found.")

    # Quit the program
    elif choice == "5":
        print("Contact list closed.")
        break

    else:
        print("Invalid option. Please try again.")
