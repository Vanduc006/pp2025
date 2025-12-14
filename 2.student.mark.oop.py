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
        self.__students = [
            Student("2411150", "Nguyen Van Duc", "28/08/2006")
        ]

        self.__courses = [
            Course("ICT.001", "Introduction"),
            Course("MAT.001", "Calculus I")
        ]

        self.__marks = {}  
        self.__marks = {}
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

        self.__marks[cid] = {}

        for s in self.__students:
            score = float(input(f"Mark for {s.getName()}: "))
            self.__marks[cid][s.getId()] = score

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

    def main(self):
        while True:
            print("""
                1. Input students
                2. Input courses
                3. List students
                4. List courses
                5. Input marks
                6. Show marks
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
                break
            else:
                print("Invalid!")

m = Management()
m.main()

