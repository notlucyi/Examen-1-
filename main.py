from student_registry import Student, StudentRegistry

registry = StudentRegistry()

while True:
    print("Student Registry")
    print("1. Add student")
    print("2. Remove student")
    print("3. Find student")
    print("4. List students")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")

        student = Student(student_id, name, age)
        registry.add_student(student)

    elif option == "2":
        student_id = input("Enter ID of student to remove: ")
        registry.remove_student(student_id)

    elif option == "3":
        student_id = input("Enter ID of student to search: ")
        registry.find_student(student_id)

    elif option == "4":
        registry.list_students()

    elif option == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid option, try again.")