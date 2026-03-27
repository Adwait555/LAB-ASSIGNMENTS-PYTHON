# practical_9_combined.py

# --- LAB ASSIGNMENT 1: EMPLOYEE & MANAGER INHERITANCE ---
class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0.0
        self.address = ""

    def get_input(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Salary: {self.salary} | Address: {self.address}")

class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def get_manager_input(self):
        self.get_input()
        self.department = input("Enter Department: ")

    def display_manager_info(self):
        self.display_info()
        print(f"Department: {self.department}")
        print("-" * 30)

def run_assignment_1():
    managers_list = []
    # Note: Reduced to 2 for quick testing, change '3' to '11' for 10 managers
    limit = 3 
    print(f"\n--- Processing {limit-1} Managers ---")
    for i in range(1, limit):
        print(f"\nManager {i}:")
        m = Manager()
        m.get_manager_input()
        managers_list.append(m)

    print("\n--- Displaying Manager Information ---")
    for m in managers_list:
        m.display_manager_info()




# --- LAB ASSIGNMENT 2: LIBRARY MANAGEMENT SYSTEM ---
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_lent = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = {}

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book '{title}' added to library.")

    def add_member(self, name):
        if name not in self.members:
            self.members[name] = Member(name)
            print(f"Member '{name}' registered.")

    def lend_book(self, member_name, book_title):
        member = self.members.get(member_name)
        if not member:
            print("Member not found.")
            return

        for book in self.books:
            if book.title == book_title and not book.is_lent:
                book.is_lent = True
                member.borrowed_books.append(book)
                print(f"Book '{book_title}' lent to {member_name}.")
                return
        print("Book not available or already lent.")

    def return_book(self, member_name, book_title):
        member = self.members.get(member_name)
        if member:
            for book in member.borrowed_books:
                if book.title == book_title:
                    book.is_lent = False
                    member.borrowed_books.remove(book)
                    print(f"Book '{book_title}' returned by {member_name}.")
                    return
        print("Record not found.")

    def display_books(self):
        print("\n--- Library Collection ---")
        if not self.books:
            print("No books in library.")
        for book in self.books:
            status = "Available" if not book.is_lent else "Lent"
            print(f"Title: {book.title} | Author: {book.author} | Status: {status}")

def run_assignment_2():
    lib = Library()
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book\n2. Register Member\n3. Lend Book\n4. Return Book\n5. Display Books\n6. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            lib.add_book(input("Title: "), input("Author: "))
        elif choice == '2':
            lib.add_member(input("Member Name: "))
        elif choice == '3':
            lib.lend_book(input("Member Name: "), input("Book Title: "))
        elif choice == '4':
            lib.return_book(input("Member Name: "), input("Book Title: "))
        elif choice == '5':
            lib.display_books()
        elif choice == '6':
            break
        else:
            print("Invalid Choice.")

# --- MAIN CONTROLLER ---
def main():
    while True:
        print("\n==============================")
        print("    PRACTICAL NO: 9 MENU")
        print("==============================")
        print("1. Run Assignment 1 (Employee/Manager Inheritance)")
        print("2. Run Assignment 2 (Library Management System)")
        print("3. Exit")
        
        main_choice = input("\nSelect Practical Assignment: ")
        
        if main_choice == '1':
            run_assignment_1()
        elif main_choice == '2':
            run_assignment_2()
        elif main_choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid Selection.")

if __name__ == "__main__":
    main()
