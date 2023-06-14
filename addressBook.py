import os

# Address book dictionary
address_book = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_contact():
    clear_screen()
    
    print("--- Add Contact ---")
    name = input("Name: ")
    phone = input("Phone Number: ")
    
    # Validate phone number
    if not phone.isdigit():
        print("Invalid phone number! Only digits are allowed.")
        input("Press enter to continue.")
        return
    occupation = input("Occupation: ")
    birthday = input("Birthday: ")
    
    # Validate birthday
    try:
        day, month, year = map(int, birthday.split('-'))
        # Additional checks can be added here, e.g., valid range for day/month/year
    except ValueError:
        print("Invalid birthday format! Please use the DD-MM-YYYY format.")
        input("Press enter to continue.")
        return
    
    email = input("Email: ")
    address = input("Address: ")
    contact = {
        'Phone': phone,
        'Occupation': occupation,
        'Birthday': birthday,
        'Email': email,
        'Address': address
    }
    
    address_book[name] = contact
    print("Contact added successfully!")

def delete_contact():
    clear_screen()
    print("--- Delete Contact ---")
    name = input("Name: ")
    if name in address_book:
        del address_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def view_contacts():
    clear_screen()
    print("********************")
    print("*** Address Book ***")
    print("********************")
    if len(address_book) > 0:
        for name, contact in address_book.items():
            print(f"Name: {name}")
            for key, value in contact.items():
                print(f"{key}: {value}")
            print("--------------------")
            print("--------------------")
    else:
        print("No contacts found!")

def clear_address_book():
    clear_screen()
    confirm = input("Are you sure you want to delete all contacts? (y/n): ")
    if confirm.lower() == 'y':
        address_book.clear()
        print("Address book cleared successfully!")
    else:
        print("Operation canceled.")

def export_contacts():
    clear_screen()
    print("--- Export Contacts ---")
    filename = input("Enter the file name (without extension): ")
    filepath = f"{filename}.txt"

    with open(filepath, 'w') as file:
        for name, contact in address_book.items():
            file.write(f"Name: {name}\n")
            for key, value in contact.items():
                file.write(f"{key}: {value}\n")
            file.write("--------------------\n")
    
    print(f"Contacts exported successfully to '{filepath}'")
    input("Press enter to continue.")

def main_menu():
    while True:
        clear_screen()
        print("--- Address Book ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View Contacts")
        print("4. Export Contacts")
        print("5. Clear Address Book")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            delete_contact()
        elif choice == '3':
            view_contacts()
        elif choice == '4':
            export_contacts()
        elif choice == '5':
            clear_address_book()
        elif choice == '6':
            clear_screen()
            print("Thank you for using the Address Book!")
            break
        else:
            input("Invalid choice! Press enter to continue.")

# Run the program
main_menu()
input("Press enter to exit...")
