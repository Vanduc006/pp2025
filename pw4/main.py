from domains.management import Management
from domains.student import Student
from domains.course import Course

import input as inp
import output as out
import os
import pickle
import json


manager = Management()

if not (os.path.exists('students.txt')):
    with open('students.txt','a') as file:
        # for students in manager.students:
        #     file.write(students.toString())
        #     file.write("\n")
        json.dump(manager.students,file,indent=4)

if not (os.path.exists('courses.txt')):
    with open('courses.txt','a') as file:
        # for course in manager.courses:
        #     file.write(course.toString())
        #     file.write("\n")
        json.dump(manager.courses,file,indent=4)


if not (os.path.exists('marks.txt')):
    with open('marks.txt','a') as file:
        json.dump(manager.marks, file, indent=4)

with open ('students.txt','r') as file:
    manager.students = json.load(file)

with open ('courses.txt','r') as file:
    manager.courses = json.load(file)

with open ('marks.txt','r') as file:
    manager.marks = json.load(file)

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
        10. Save
    """)
    choice = input("Choose: ")
    os.system('clear')
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
        out.listCourses(manager)
        out.listMarks(manager)
    elif choice == '7':
        out.listStudents(manager)
        sid = input("Student ID: ")
        print("GPA:", manager.calculateGPA(sid))
    elif choice == '8':
        out.sortByGPA(manager)
    elif choice == '9':
        break
    elif choice == '10':
        compressType = str(input("Type to compress (DAT/PICKLE)"))
        # if compressType == "DAT" or compressType == "dat":
        #     with open("") as file:

    else:
        print("Invalid choice!")


