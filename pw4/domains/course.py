class Course:
    def __init__(self, id="", name="", credit="4"):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course name: ")

    def toString(self):
        return f"{self.__id} | {self.__name} | {self.__credit}"

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getCredit(self):
        return self.__credit
