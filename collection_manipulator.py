

students = []

print("Welcome to the Student Data Organizer!")

while True:

    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:

        print("Enter student details:")

        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")

        subjects_input = input("Subjects (comma-separated): ")

        subjects = set()

        for subject in subjects_input.split(","):
            subjects.add(subject.strip())

        
        student_details = (student_id, dob)

    
        student = {
            "details": student_details,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        
        students.append(student)

        print("Student added successfully!")

    
    elif choice == 2:

        print("--- Display All Students ---")

        if len(students) == 0:
            print("No student records found.")

        else:
            for student in students:

                student_id, dob = student["details"]

                print(
                    "Student ID:", student_id,
                    "| Name:", student["name"],
                    "| Age:", student["age"],
                    "| Grade:", student["grade"],
                    "| DOB:", dob,
                    "| Subjects:", ", ".join(student["subjects"])
                )

    
    elif choice == 3:

        student_id = int(input("Enter Student ID to update: "))

        found = False

        for student in students:

            if student["details"][0] == student_id:

                print("Student found.")

                new_age = int(input("Enter new age: "))
                new_subjects = input(
                    "Enter new subjects (comma-separated): "
                )

                student["age"] = new_age

                new_set = set()

                for subject in new_subjects.split(","):
                    new_set.add(subject.strip())

                student["subjects"] = new_set

                print("Student information updated successfully!")

                found = True
                break

        if found == False:
            print("Student ID not found.")

    
    elif choice == 4:

        student_id = int(input("Enter Student ID to delete: "))

        found = False

        for i in range(len(students)):

            if students[i]["details"][0] == student_id:

                del students[i]

                print("Student deleted successfully!")

                found = True
                break

        if found == False:
            print("\nStudent ID not found.")

    
    elif choice == 5:

        all_subjects = set()

        for student in students:
            all_subjects.update(student["subjects"])

        print("--- Subjects Offered ---")

        if len(all_subjects) == 0:
            print("No subjects found.")

        else:
            for subject in sorted(all_subjects):
                print(subject)

    
    elif choice == 6:

        print("Thank you for using the Student Data Organizer!")
        break

    else:

        print("Invalid choice. Please try again.")