contacts = []
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print(f"\nContact '{name}' added successfully.\n")
def view_contacts():
    if contacts:
        print("\nContact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("\nNo contacts found.\n")
def search_contact():
    query = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if query in contact['name'] or query in contact['phone']]
    
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("\nNo contact found with that information.\n")

# Function to update a contact
def update_contact():
    query = input("Enter the name or phone number of the contact you want to update: ")
    for contact in contacts:
        if query == contact['name'] or query == contact['phone']:
            print(f"\nCurrent details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            contact['name'] = input("Enter new name: ")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email address: ")
            contact['address'] = input("Enter new address: ")
            print("\nContact updated successfully.\n")
            return
    print("\nNo contact found with that information.\n")
def delete_contact():
    query = input("Enter the name or phone number of the contact you want to delete: ")
    for contact in contacts:
        if query == contact['name'] or query == contact['phone']:
            contacts.remove(contact)
            print("\nContact deleted successfully.\n")
            return
    print("\nNo contact found with that information.\n")
def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
