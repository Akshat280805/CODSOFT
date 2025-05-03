contacts = []

def show_menu():
    print("\n=== CONTACT BOOK ===")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    print("\n-- Add a New Contact --")
    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print(f"Contact for {name} added successfully!")

def list_contacts():
    print("\n-- Contact List --")
    if not contacts:
        print("No contacts saved yet.")
        return

    for idx, contact in enumerate(contacts):
        print(f"{idx+1}. {contact['name']} - {contact['phone']}")

def find_contact(query):
    matches = []
    for c in contacts:
        if query.lower() in c['name'].lower() or query in c['phone']:
            matches.append(c)
    return matches

def search_contact():
    print("\n-- Search Contact --")
    term = input("Enter name or phone number: ").strip()
    results = find_contact(term)

    if results:
        for contact in results:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
    else:
        print("No matching contact found.")

def update_contact():
    print("\n-- Update Contact --")
    term = input("Enter name or phone number to update: ").strip()
    found = find_contact(term)

    if not found:
        print("No contact found with that info.")
        return

    contact = found[0]
    print(f"Editing {contact['name']}")
    contact['name'] = input(f"New name (leave blank to keep '{contact['name']}'): ") or contact['name']
    contact['phone'] = input(f"New phone (leave blank to keep '{contact['phone']}'): ") or contact['phone']
    contact['email'] = input(f"New email (leave blank to keep '{contact['email']}'): ") or contact['email']
    contact['address'] = input(f"New address (leave blank to keep '{contact['address']}'): ") or contact['address']
    print("Contact updated.")

def delete_contact():
    print("\n-- Delete Contact --")
    term = input("Enter name or phone number to delete: ").strip()
    found = find_contact(term)

    if not found:
        print("Couldn't find any contact to delete.")
        return

    contact = found[0]
    confirm = input(f"Are you sure you want to delete contact '{contact['name']}'? (yes/no): ").strip().lower()
    if confirm == 'yes':
        contacts.remove(contact)
        print("Contact deleted.")
    else:
        print("Deletion cancelled.")

def contact_book():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            list_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try 1–6.")

if __name__ == "__main__":
    contact_book()
