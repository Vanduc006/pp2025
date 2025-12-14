from domains.management import Management
import input as inp
import output as out

def main():
    manager = Management()

    while True:
        print("""
1. Input students
2. Input courses
3. List students
4. List courses
5. Input marks
6. Show marks
7. GPA by student ID
8. Sort by GPA
9. Exit
""")
        choice = input("Choose: ")

        if choice == '1':
            inp.inputStudents(manager)
        elif choice == '2':
            inp.inputCourses(manager)
        elif choice == '3':
            out.listStudents(manager)
        elif choice == '4':
            out.listCourses(manager)
        elif choice == '5':
            inp.inputMarks(manager)
        elif choice == '6':
            out.listMarks(manager)
        elif choice == '7':
            sid = input("Student ID: ")
            print("GPA:", manager.calculateGPA(sid))
        elif choice == '8':
            out.sortByGPA(manager)
        elif choice == '9':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
