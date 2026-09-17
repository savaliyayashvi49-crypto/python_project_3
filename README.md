📚 Student Data Organizer

A small Python project made to keep student information organized in one place.

Instead of maintaining separate details, this program stores a student's basic information and subjects together. It works through a simple menu, so the user can choose what operation to perform.

---

🎯 What This Program Does

The program can:

- ➕ Add a new student
- 📋 Show all saved students
- ✏️ Change a student's age and subjects
- 🗑️ Remove a student
- 📚 Find all subjects currently entered
- 🚪 Exit the program

---

🧩 Collection Types in My Project

One of the main purposes of this project is to use different Python collections together.

Collection| Used For
List| Stores all student records
Dictionary| Stores information of one student
Tuple| Keeps Student ID and DOB together
Set| Stores subjects without repeated values

How the data is arranged

Students List
      │
      └── Student Dictionary
             │
             ├── Details → (Student ID, DOB)
             ├── Name
             ├── Age
             ├── Grade
             └── Subjects → {Set}

---

🖥️ Program Menu

Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

---

✨ Some Useful Parts

1. Adding a Student

The user enters:

Student ID
Name
Age
Grade
Date of Birth
Subjects

Subjects are entered using commas, for example:

Python, Maths, Physics

The program separates them and stores them as a set.

2. Avoiding Duplicate Subjects

Since subjects are stored in a set, repeated subjects are not kept multiple times.

Example:

Python, Maths, Python, Physics

becomes:

Python
Maths
Physics

3. Updating Information

The Student ID is used to find the required student.

The program then allows the user to enter:

- New Age
- New Subjects

4. Deleting a Student

The Student ID is used to locate the record, and that student's record is removed from the main list.

5. Subjects Offered

The program collects subjects from all students into one set.

This makes it possible to display each subject only once.

---

🔧 Python Concepts Used

This project uses:

- Variables
- "input()"
- "print()"
- "if-elif-else"
- "while" loop
- "for" loop
- List
- Dictionary
- Tuple
- Set
- "append()"
- "del"
- "split()"
- "strip()"
- "update()"
- "sorted()"
- "len()"

---

▶️ How to Start

1. Open the Python file.
2. Run the program.
3. Choose an option from 1 to 6.
4. Enter the requested information.
5. Continue using the menu until you select 6.

---

💡 Project Idea

The idea behind this project is simple:

Enter → Store → View → Update → Delete

It is a small example of how Python collection data types can be combined to handle student information.

---

📝 Note

This project is created using basic Python concepts and does not require any external library or database.

Project: Student Data Organizer
Language: Python
Type: Menu-Based Program
Main Topic: Collection Manipulation


