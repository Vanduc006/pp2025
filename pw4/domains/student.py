class Student:
    def __init__(self, id="", name="", dob=""):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def input(self):
        self.__id = input("Student ID: ")
        self.__name = input("Student name: ")
        self.__dob = input("Student DOB: ")

    def toString(self):
        return f"{self.__id} | {self.__name} | {self.__dob}"

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
