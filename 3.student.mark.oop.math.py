import math
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        self.__id = id 
        self.__name = name 
        self.__dob = dob

    def input(self):
        self.__id = str(input("Student ID"))
        self.__name = str(input("Student name"))
        self.__dob = str(input("Student Dob"))
    def toString(self):
        return f"{self.__id}|{self.__name}|{self.__dob}"
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name

class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    def input(self):
        self.__id = str(input("Class ID"))
        self.__name = str(input("Class name"))
    def toString(self):
        return f"{self.__id}|{self.__name}"
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name

class Management:
    def __init__(self):
        # constant
        self.__students = [
            Student("S001", "Nguyen Van A", "01/01/2004"),
            Student("S002", "Tran Thi B", "12/05/2004"),
            Student("S003", "Le Van C", "23/09/2003"),
        ]

        self.__courses = [
            Course("ICT.001", "Introduction to ICT"),
            Course("MAT.001", "Calculus I"),
            Course("PHY.001", "Physics I"),
        ]

        self.__marks = {
            "ICT.001": {
                "S001": 8.5,
                "S002": 7.0,
                "S003": 9.0
            },
            "MAT.001": {
                "S001": 7.5,
                "S002": 6.0,
                "S003": 8.0
            },
            "PHY.001": {
                "S001": 9.0,
                "S002": 8.5
            }
        }

    def inputStudents(self):
        n = int(input("Number of new student"))
        for i in range(n):
            s = Student("","","")
            s.input()
            self.__students.append(s)
    def inputCourses(self):
        n = int(input("Number of new course"))
        for i in range(n):
            c = Course("","")
            c.input()
            self.__courses.append(c)
    def listStudents(self):
        for i in self.__students:
            print(i.toString())
    def listCourses(self):
        for i in self.__courses:
            print(i.toString())

    def inputMarks(self):
        self.listCourses()
        cid = input("Select course ID: ")

        self.marks[cid] = {}

        for s in self.__students:
            score = float(input(f"Mark for {s.getName()}: "))
            self.__marks[cid][s.getId()] = self.roundedDigits(score)

    def listMarks(self):
        self.listCourses()
        cid = input("Show marks for course ID: ")

        if cid not in self.__marks:
            print("No marks recorded.")
            return

        print(f"\n=== Marks for {cid} ===")
        for s in self.__students:
            sid = s.getId()
            print(f"{s.getName()}: {self.__marks[cid].get(sid, 'N/A')}")

    def roundedDigits(self,score):
        rounded = 10 ** 1
        return math.floor(score*rounded) / rounded
    
    def calculateGPA(self,studentID):
        score = []
        for marks in self.__marks.values():
            if studentID in marks:
                score.append(marks[studentID])
        # if not score:
        #     return None
        scoreNp = np.array(score)
        studentGPA = round(np.mean(scoreNp),2)
        return studentGPA
    
    def sortGPA(self):
        listGPA = []
        for s in self.__students:
            gpa = self.calculateGPA(s.getId())
            if gpa is not None:
                listGPA.append((s.getId(), s.getName(), gpa))
        listGPA.sort(key = lambda x:x[2], reverse=True) 
        for studentID, studentName, studentGPA in listGPA:
            print(f"{studentID} | {studentName} : {studentGPA}")
    
    def main(self):
        while True:
            print("""
                1. Input students
                2. Input courses
                3. List students
                4. List courses
                5. Input marks
                6. Show marks
                7. GPA by studentID
                8. Sort by GPA
                7. Exit
                """)
            choice = input("Choose: ")

            if choice == '1':
                self.inputStudents()
            elif choice == '2':
                self.inputCourses()
            elif choice == '3':
                self.listStudents()
            elif choice == '4':
                self.listCourses()
            elif choice == '5':
                self.inputMarks()
            elif choice == '6':
                self.listMarks()
            elif choice == '7':
                studentID = str(input("Student ID to get GPA: "))
                self.calculateGPA(studentID)
            elif choice == '8':
                self.sortGPA()
            else:
                print("Invalid!")

m = Management()
m.main()

