#  this code creates a Student class for use in the program

class Student:

    def __init__(self, student_name):

        """ constructor of class Student """

        self.name = student_name
        self.project = 0.0
        self.midterm = 0.0

    def inputScores(self):

        """ input scores from user """

        self.project = float(input("Enter project score: "))
        self.midterm = float(input("Enter midterm score: "))
        self.final = float(input("Enter final score: "))

    def calcAvg(self):

        """ return average of 3 scores """

        avg = (self.project + self.midterm + self.final)/3
        return avg
