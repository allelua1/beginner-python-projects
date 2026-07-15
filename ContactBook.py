"""
Simple Contact Book
Store contacts in a dictionary {name: phone}.
Functions: add, delete, search, display all. Uses a loop for the menu.
"""

def add_contact(contacts, name, phonenumber):
    """Add or update a contact and print a confirmation."""
    contacts[name] = phonenumber
    print(f"Added/Updated contact: {name} -> {phonenumber}")


def delete_contact(contacts, name):
    """Delete a contact if it exists."""
    if name in contacts:
        contacts.pop(name)
        print(f"{name} has been deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")


def search_contact(contacts, name):
    """Search and print a contact's phone number."""
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")


def display_all_contact(contacts):
    """Display all contacts sorted by name."""
    if not contacts:
        print("No contacts saved.")
        return
    print("All contacts:")
    for name, phonenumber in sorted(contacts.items()):
        print(name, ":", phonenumber)


def main():
    contacts = {
        "Benigne": "07949811382",
        "Diane": "08948785895",
        "Sandy": "0997577805",
    }

    while True:
        print("\nContact Book Menu")
        print("1. Display all contacts")
        print("2. Delete contact")
        print("3. Search contact")
        print("4. Add contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Your choice should be a number. Try again.")
            continue

        if choice == 1:
            display_all_contact(contacts)
        elif choice == 2:
            name = input("Enter the name of the contact you want to delete: ").strip()
            delete_contact(contacts, name)
        elif choice == 3:
            name = input("Enter the name to search: ").strip()
            search_contact(contacts, name)
        elif choice == 4:
            name = input("Enter contact name: ").strip()
            phonenumber = input("Enter phone number: ").strip()
            add_contact(contacts, name, phonenumber)
        elif choice == 5:
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
    





    