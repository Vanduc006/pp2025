from domains.student import Student
from domains.course import Course

def inputStudents(manager):
    n = int(input("Number of new students: "))
    for _ in range(n):
        s = Student()
        s.input()
        manager.students.append(s)

def inputCourses(manager):
    n = int(input("Number of new courses: "))
    for _ in range(n):
        c = Course()
        c.input()
        manager.courses.append(c)

def inputMarks(manager):
    for c in manager.courses:
        print(c.toString())

    cid = input("Select course ID: ")
    manager.marks[cid] = {}

    for s in manager.students:
        score = float(input(f"Mark for {s.getName()}: "))
        manager.marks[cid][s.getId()] = manager.roundedDigits(score)
