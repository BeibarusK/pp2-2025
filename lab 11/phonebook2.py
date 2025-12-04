import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="phonebook1",
        user="postgres",
        password="1845" 
    )

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    print("Added!")

def query_with_pagination(limit, offset):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name, phone FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
            return cur.fetchall() 
    
def insert_many_users():
    users = []
    incorrect = []

    print("Enter users (name and phone). Type 'q' to finish.\n")

    while True:
        name = input("Name (or 'q'): ")
        if name.lower() == "q":
            break

        phone = input("Phone: ")
        users.append((name, phone))
        print("User added.\n")

    with connect() as conn:
        with conn.cursor() as cur:
            for name, phone in users:

                if not phone.isdigit():
                    incorrect.append((name, phone))
                    continue

                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                    (name, phone)
                )

    print("\nFinished")
    if incorrect:
        print("Incorrect data:")
        for name, phone in incorrect:
            print(f"{name} - {phone}")
    else:
        print("All users inserted correctly.")

def return_by_pattern():
    pattern = input("Enter pattern: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute()

def insert_from_csv(path):
    with connect() as conn:
        with conn.cursor() as cur:
            with open(path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    print("CSV imported!")

def update_user(name, new_phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    print("Updated!")

def query_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook")
            for row in cur.fetchall():
                print(row)

def search_by_pattern(pattern):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s",
                (f"%{pattern}%", f"%{pattern}%")
            )
            return cur.fetchall()

def delete_user(name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    print("Deleted!")

def delete_user_by_phone(phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    print("Deleted!")

def menu():
    while True:
        print("\n1. Insert (console)")
        print("2. Insert (CSV)")
        print("3. Update user")
        print("4. View all")
        print("5. Search by pattern")
        print("6. Delete user(by name)")
        print("7. Delete user(by phone)")
        print("8. Insert many users")
        print("9. Query with pagination")
        print("10. Exit")

        choice = input("Choose: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv(input("Enter CSV path: "))
        elif choice == '3':
            update_user(input("Name to update: "), input("New phone: "))
        elif choice == '4':
            query_all()
        elif choice == '5':
            pattern = input("Pattern: ")
            rows = search_by_pattern(pattern)
            for row in rows:
                print(row)
        elif choice == '6':
            delete_user(input("Name to delete: "))
        elif choice == '7':
            delete_user_by_phone(input("Phone to delete: "))
        elif choice == '8':
            insert_many_users()
        elif choice == '9':
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            rows = query_with_pagination(limit, offset)
            for row in rows:
                print(row)
        elif choice == '10':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()