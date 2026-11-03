import csv
from connect import connect, create_table


def insert_contact():
    first = input("First name: ")
    last = input("Last name: ")
    phone = input("Phone: ")
    city = input("City: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO contacts (first_name, last_name, phone, city)
        VALUES (%s, %s, %s, %s)
    """, (first, last, phone, city))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added!")


def import_csv():
    conn = connect()
    cur = conn.cursor()

    try:
        with open("contacts.csv", "r") as file:
            reader = csv.DictReader(file)

            data = [
                (row["first_name"], row["last_name"],
                 row["phone"], row["city"])
                for row in reader
            ]

        cur.executemany("""
            INSERT INTO contacts (first_name, last_name, phone, city)
            VALUES (%s, %s, %s, %s)
        """, data)

        conn.commit()
        print("CSV imported!")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts ORDER BY id")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def search_contact():
    value = input("Enter name, surname, phone prefix or city: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM contacts
        WHERE first_name ILIKE %s
        OR last_name ILIKE %s
        OR phone LIKE %s
        OR city ILIKE %s
    """, (f"%{value}%", f"%{value}%", f"{value}%", f"%{value}%"))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def update_contact():
    phone = input("Enter current phone: ")

    print("1. Update first name")
    print("2. Update last name")
    print("3. Update phone")
    print("4. Update city")

    choice = input("Choose: ")

    columns = {
        "1": "first_name",
        "2": "last_name",
        "3": "phone",
        "4": "city"
    }

    if choice not in columns:
        print("Invalid choice!")
        return

    value = input("Enter new value: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        f"UPDATE contacts SET {columns[choice]} = %s WHERE phone = %s",
        (value, phone)
    )

    conn.commit()
    print("Updated!")

    cur.close()
    conn.close()


def delete_contact():
    value = input("Enter username or phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM contacts
        WHERE first_name || ' ' || last_name = %s
        OR phone = %s
    """, (value, value))

    conn.commit()
    print("Deleted!")

    cur.close()
    conn.close()


def menu():
    create_table()

    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Add contact")
        print("2. Import CSV")
        print("3. Show contacts")
        print("4. Search contact")
        print("5. Update contact")
        print("6. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_contact()
        elif choice == "2":
            import_csv()
        elif choice == "3":
            show_contacts()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()