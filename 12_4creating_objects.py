class Student:

    def __init__(self, student_name):

        self.name = student_name
        self.project = 0.0
        self.midterm = 0.0
        self.final = 0.0


    def inputScores(self):

        self.project = float(input("Enter project score: "))
        self.midterm = float(input("Enter midterm score: "))
        self.final = float(input("Enter final score: "))


    def calcAvg(self):

        avg = (self.project + self.midterm + self.final)/3
        return avg


def main():

    name = input("Enter student name: ")
    student1 = Student(name)
    student1.inputScores()
    average = student1.calcAvg()
    print("Average score of this student: ", average)

    name = input("Enter student name: ")
    student2 = Student(name)
    student2.inputScores()
    average = student2.calcAvg()
    print("Average score of this student: ", average)


main()
