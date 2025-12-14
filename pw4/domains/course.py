class Course:
    def __init__(self, id="", name=""):
        self.__id = id
        self.__name = name

    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course name: ")

    def toString(self):
        return f"{self.__id} | {self.__name}"

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
