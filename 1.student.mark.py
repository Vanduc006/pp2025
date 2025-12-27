students = [
    {
        "id":"2411150",
        "name":"Nguyen Van Duc",
        "dob":"28/08/2006"
    }
]
courses = [
    {
        "id":"ICT.001",
        "name":"Introduction"
    },
    {
        "id":"MAT.001",
        "name":"CalculusI"
    }
]        
marks = {}           

def input_number_of_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        input_student_info()

def input_student_info():
    sid = input("Student ID: ")
    name = input("Student name: ")
    dob = input("Date of birth: ")

    student = {"id": sid, "name": name, "dob": dob}
    students.append(student)

def input_number_of_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        input_course_info()

def input_course_info():
    cid = input("Course ID: ")
    cname = input("Course name: ")

    course = {"id": cid, "name": cname}
    courses.append(course)

def select_course_and_input_marks():
    print("\nAvailable courses:")
    list_courses()

    cid = input("Enter course ID to input marks: ")

    # create mark storage if not exists
    if cid not in marks:
        marks[cid] = {}

    print("\nInput marks for each student:")
    for s in students:
        mark = float(input(f"Mark for {s['name']} ({s['id']}): "))
        marks[cid][s["id"]] = mark

def list_courses():
    print("\nCourse List")
    for c in courses:
        print(f"- {c['id']}: {c['name']}")

def list_students():
    print("\nStudent List")
    for s in students:
        print(f"- {s['id']} | {s['name']} | DoB: {s['dob']}")

def show_student_marks_by_course():
    print("\nCourses")
    list_courses()
    cid = input("Select course ID: ")

    if cid not in marks:
        print("No marks available for this course yet.")
        return

    print(f"\n--- Marks for Course {cid} ---")
    for s in students:
        sid = s["id"]
        m = marks[cid].get(sid, "N/A")
        print(f"{s['name']} ({sid}): {m}")

def main():
    while True:
        print("""
1. Input students
2. Input courses
3. Input marks for a course
4. List all students
5. List all courses
6. Show marks for a course
7. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            input_number_of_students()
        elif choice == "2":
            input_number_of_courses()
        elif choice == "3":
            select_course_and_input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_student_marks_by_course()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option!")

main()
