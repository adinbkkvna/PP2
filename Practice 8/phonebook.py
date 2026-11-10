from connect import connect, create_table
def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def search_contact():
    pattern = input("Enter name, surname or phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM get_contacts_by_pattern(%s)",
        (pattern,)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def add_or_update_contact():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone (+7XXXXXXXXXX): ")

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "CALL upsert_contact(%s, %s, %s)",
        (first_name, last_name, phone)
    )

    conn.commit()
    print("Contact saved!")
    cur.close()
    conn.close()


def delete_contact():
    value = input("Enter full name or phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "CALL delete_contact(%s)",
        (value,)
    )
    conn.commit()
    cur.close()
    conn.close()


def show_page():
    limit = int(input("How many contacts? "))
    offset = int(input("How many contacts to skip? "))

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM get_contacts_page(%s, %s)",
        (limit, offset)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def menu():
    while True:
        print("\nPHONEBOOK")
        print("1. Show all contacts")
        print("2. Search contact")
        print("3. Add or update contact")
        print("4. Delete contact")
        print("5. Show contacts by pages")
        print("0. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            show_contacts()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            add_or_update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            show_page()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")
            
if __name__ == "__main__":
    create_table()
    menu()
