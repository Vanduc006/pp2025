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

class Ultil:
    def __init__(self):
        pass
        
class Management:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def existById(self,id,domain:str): 
        if (domain == "students"):
            for i in self.__students:
                if (i.getId() == id):
                    return True
        if (domain == "courses"):
            for i in self.__courses:
                if (i.getId() == id):
                    return True
        return False

    def isBlank(self, domain:str):
        if (domain == "students"):
            if (self.__students == []):
                return True      
        if (domain == "courses"):
            if (self.__courses == []):
                return True
        return False
        
    def inputStudents(self):
        # Avoid duplicate id
        n = int(input("Number of new student"))
        for i in range(n):
            s = Student("","","")
            s.input()
            if (self.existById(s.getId(),"students")) :
                print("Student id already exists")
                return
            self.__students.append(s)

    def inputCourses(self):
        # Avoid duplicate id
        n = int(input("Number of new course"))
        for i in range(n):
            c = Course("","")
            c.input()
            if (self.existById(c.getId(),"courses")):
                print("Course id already exists")
                return
            self.__courses.append(c)

    def listStudents(self):
        # Blank students lists
        if (self.isBlank("students")):
            print("List student is null")
        
        for i in self.__students:
            print(i.toString())
            
    def listCourses(self):
        if (self.isBlank("courses")):
            print("List course is null")
        for i in self.__courses:
            print(i.toString())

    def inputMarks(self):
        if (self.isBlank("courses")):
            print("Not exists any course")
            return
        if (self.isBlank("students")):
            print("Not exists any students")
            return

        self.listCourses()
        cid = input("Select course ID: ")
        if (self.existById(cid) == False):
            print("Course not exists")
        self.__marks[cid] = {}

        for s in self.__students:
            score = float(input(f"Mark for {s.getName()}: "))
            self.__marks[cid][s.getId()] = score

    def listMarks(self):
        self.listCourses()
        cid = input("Show marks for course ID: ")

        if cid not in self.__marks:
            print("No marks recorded")
            return

        print(f"\nMarks for {cid}")
        for s in self.__students:
            sid = s.getId()
            print(f"{s.getName()}: {self.__marks[cid].get(sid, 'N/A')}")
        

def main():
    m = Management()
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
            m.inputStudents()
        elif choice == '2':
            m.inputCourses()
        elif choice == '3':
            m.listStudents()
        elif choice == '4':
            m.listCourses()
        elif choice == '5':
            m.inputMarks()
        elif choice == '6':
            m.listMarks()
        elif choice == '7':
            break
        else:
            print("Invalid!")

main()