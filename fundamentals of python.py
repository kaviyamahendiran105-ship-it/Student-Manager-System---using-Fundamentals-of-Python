students = []

# Function to add student
def add_student():
    print("\n--- Add Student ---")

    id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")

    marks = []
    for i in range(3):
        mark = int(input(f"Enter mark {i+1}: "))
        marks.append(mark)

    course = input("Enter Course: ")

    student = {
        "id": id,
        "name": name,
        "marks": marks,
        "course": course
    }

    students.append(student)
    print("Student added successfully.\n")


# Function to display students
def display_students():
    print("\n--- Student List ---")

    if not students:
        print("No students found.\n")
        return

    for s in students:
        avg = sum(s["marks"]) / len(s["marks"])
        print(f"ID: {s['id']} | Name: {s['name']} | Marks: {s['marks']} | Avg: {avg}")
    print()


# Function to find top student
def top_student():
    print("\n--- Top Student ---")

    if not students:
        print("No data.\n")
        return

    top = students[0]
    for s in students:
        if sum(s["marks"]) > sum(top["marks"]):
            top = s

    print(f"Top Student: {top['name']} with marks {top['marks']}\n")


# Search student using iteration
def search_student():
    print("\n--- Search Student ---")

    name = input("Enter name to search: ")

    for s in students:
        if s["name"].lower() == name.lower():
            print("Found:", s)
            return

    print("Student not found.\n")


# Delete student
def delete_student():
    print("\n--- Delete Student ---")

    id = int(input("Enter Student ID to delete: "))

    for s in students:
        if s["id"] == id:
            students.remove(s)
            print("Deleted successfully.\n")
            return

    print("Student not found.\n")


# Main Menu
def main():
    while True:
        print("\n===== STUDENT MANAGER =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Top Student")
        print("4. Search Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            top_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.\n")


main()
