import math
import numpy as np
from domains.student import Student
from domains.course import Course

class Management:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
        # self.students = [
        #     Student("S001", "Nguyen Van A", "01/01/2004"),
        #     Student("S002", "Tran Thi B", "12/05/2004"),
        #     Student("S003", "Le Van C", "23/09/2003"),
        # ]

        # self.courses = [
        #     Course("ICT.001", "Introduction to ICT","4"),
        #     Course("MAT.001", "Calculus I","4"),
        #     Course("PHY.001", "Physics I","4"),
        # ]

        # self.marks = {
        #     "ICT.001": {"S001": 8.5, "S002": 7.0, "S003": 9.0},
        #     "MAT.001": {"S001": 7.5, "S002": 6.0, "S003": 8.0},
        #     "PHY.001": {"S001": 9.0, "S002": 8.5},
        # }

    def roundedDigits(self, score):
        return math.floor(score * 10) / 10

    def calculateGPA(self, studentID):
        totalWeightedScore = 0
        totalCredit = 0

        for courseId, courseMarks in self.marks.items():
            if studentID in courseMarks:
                score = courseMarks[studentID]
                credit = 0
                for course in self.courses:
                    if course.getId() == courseId:
                        credit = course.getCredit()
                        break

                totalWeightedScore += int(score) * int(credit)
                totalCredit += int(credit)

        return self.roundedDigits(totalWeightedScore/totalCredit)


