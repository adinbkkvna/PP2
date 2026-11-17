import json
import csv
from datetime import date
from connect import connect, create_table
def filter_by_group():
    group = input("Enter group (Family,Work,Friend,Other):")

    print("\nSort by:")
    print("1. Name")
    print("2. Birthday")
    print("3. Date added")

    choice = input("Choose sorting:")

    sort_options = {
        "1": "c.first_name ASC",
        "2": "c.birthday ASC NULLS LAST",
        "3": "c.date_added DESC"
    }
    if choice not in sort_options:
        print("Invalid sorting option")
        return

    conn = connect()
    cur = conn.cursor()

    query = f"""
        SELECT
            c.id,
            c.first_name,
            c.last_name,
            c.email,
            c.birthday,
            g.name,
            COALESCE(
                STRING_AGG(p.phone || ' (' || p.type || ')', ', '),
                ''
            )
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        WHERE g.name ILIKE %s
        GROUP BY c.id, g.name
        ORDER BY {sort_options[choice]}
    """

    cur.execute(query, (group,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def search_by_email():
    email = input("Enter email or part of email:")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            c.id,
            c.first_name,
            c.last_name,
            c.email,
            c.birthday,
            g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        WHERE c.email ILIKE %s
        ORDER BY c.first_name
        """,
        ('%'+ email +'%',)
    )

    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found")

    cur.close()
    conn.close()

def paginate_contacts():
    limit = 5
    offset = 0

    while True:
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM get_contacts_page(%s, %s)",
            (limit, offset)
        )
        rows = cur.fetchall()

        cur.close()
        conn.close()

        print("\n--- CONTACTS ---")

        if not rows:
            print("No contacts on this page")
        else:
            for row in rows:
                print(row)

        print("\nnext -Next page")
        print("prev -Previous page")
        print("quit -Exit pagination")

        command = input("Choose command:").lower()

        if command == "next":
            offset += limit

        elif command == "prev":
            offset = max(0, offset - limit)

        elif command == "quit":
            break
        else:
            print("Invalid command")

def export_to_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.first_name, c.last_name,
               c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        ORDER BY c.id
    """)
    contacts = cur.fetchall()
    result = []

    for contact in contacts:
        cur.execute("""
            SELECT phone, type
            FROM phones
            WHERE contact_id = %s
        """, (contact[0],))

        phones = cur.fetchall()
        result.append({
            "first_name": contact[1],
            "last_name": contact[2],
            "email": contact[3],
            "birthday": contact[4].isoformat() if contact[4] else None,
            "group": contact[5],
            "phones": [
                {"phone": p[0], "type": p[1]}
                for p in phones
            ]
        })
    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
    cur.close()
    conn.close()
    print("Contacts exported successfully")

def import_from_json():
    try:
        with open("contacts.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("contacts.json not found!")
        return
    conn = connect()
    cur = conn.cursor()

    try:
        for contact in data:
            first_name = contact["first_name"]
            last_name = contact["last_name"]
            email = contact.get("email")
            birthday = (
                date.fromisoformat(contact["birthday"])
                if contact.get("birthday") else None
            )
            group_name = contact.get("group")
            phones = contact.get("phones", [])
            group_id = None
            if group_name:
                cur.execute("""
                    INSERT INTO groups(name)
                    VALUES (%s)
                    ON CONFLICT (name) DO NOTHING
                """, (group_name,))
                cur.execute(
                    "SELECT id FROM groups WHERE name = %s",
                    (group_name,)
                )
                group_id = cur.fetchone()[0]
            cur.execute("""
                SELECT id
                FROM contacts
                WHERE first_name = %s AND last_name = %s
                ORDER BY id
                LIMIT 1
            """, (first_name, last_name))
            existing = cur.fetchone()
            if existing:
                print(f"{first_name} {last_name} already exists!")
                choice = input("Choose skip or overwrite: ").lower()

                if choice == "skip":
                    continue
                elif choice == "overwrite":
                    contact_id = existing[0]
                    cur.execute("""
                        UPDATE contacts
                        SET email = %s,
                            birthday = %s,
                            group_id = %s,
                            phone = %s
                        WHERE id = %s
                    """, (
                        email,
                        birthday,
                        group_id,
                        phones[0]["phone"] if phones else "",
                        contact_id
                    ))

                    cur.execute(
                        "DELETE FROM phones WHERE contact_id = %s",
                        (contact_id,)
                    )
                else:
                    print("Invalid choice. Contact skipped.")
                    continue
            else:
                cur.execute("""
                            INSERT INTO contacts(
                            first_name, last_name, email, birthday, group_id
                            )
                            VALUES (%s, %s, %s, %s, %s)
                            RETURNING id
                """, (
                    first_name,
                    last_name,
                    phones[0]["phone"] if phones else "",
                    email,
                    birthday,
                    group_id
                ))
                contact_id = cur.fetchone()[0]

            for phone in phones:
                cur.execute("""
                    INSERT INTO phones(contact_id, phone, type)
                    VALUES (%s, %s, %s)
                """, (
                    contact_id,
                    phone["phone"],
                    phone["type"]
                ))
        conn.commit()
        print("Contacts imported successfully")

    except Exception as error:
        conn.rollback()
        print("Import error:", error)
    finally:
        cur.close()
        conn.close()

def import_from_csv():
    conn = None
    cur = None
    try:
        print("CSV IMPORT STARTED")

        with open("contacts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            conn = connect()
            cur = conn.cursor()
            for row in reader:
                first_name = row["first_name"]
                last_name = row["last_name"]
                email = row["email"]
                birthday = row["birthday"] or None
                group_name = row["group"]
                phone = row["phone"]
                phone_type = row["type"]

                cur.execute("""
                    INSERT INTO groups(name)
                    VALUES (%s)
                    ON CONFLICT (name) DO NOTHING
                """, (group_name,))

                cur.execute(
                    "SELECT id FROM groups WHERE name = %s",
                    (group_name,)
                )
                group_id = cur.fetchone()[0]

                cur.execute("""
                    SELECT id FROM contacts
                    WHERE first_name = %s AND last_name = %s
                    LIMIT 1
                """, (first_name, last_name))

                existing = cur.fetchone()

                if existing:
                    print(first_name, last_name, "already exists. Skipped.")
                    continue

                cur.execute("""
                    INSERT INTO contacts(
                        first_name, last_name, email, birthday, group_id
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id
                """, (first_name, last_name, email, birthday, group_id))
                contact_id = cur.fetchone()[0]
                cur.execute("""
                    INSERT INTO phones(contact_id, phone, type)
                    VALUES (%s, %s, %s)
                """, (contact_id, phone, phone_type))
            conn.commit()
            print("CSV imported successfully")
    except Exception as error:
        if conn:
            conn.rollback()
        print("CSV import error:", error)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def menu():
    while True:
        print("\nPHONEBOOK")
        print("1. Filter by group and sort")
        print("2. Search by email")
        print("3. Paginated navigation")
        print("4. Export contacts to JSON")
        print("5. Import contacts from JSON")
        print("6. Import contacts from CSV")
        print("0. Exit")
        choice = input("Choose an option:")
        if choice == "1":
            filter_by_group()
        elif choice == "2":
            search_by_email()
        elif choice == "3":
            paginate_contacts()
        elif choice == "4":
            export_to_json()
        elif choice == "5":
            import_from_json()
        elif choice == "6":
            import_from_csv()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()