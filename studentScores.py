from student import Student


def main():

    name = input("Enter student name: ")
    student1 = Student(name)
    student1.inputScores()
    average = student1.calcAvg()
    print("Average score of", student1.name, "is:", average)

    name = input("Enter student name: ")
    student2 = Student(name)
    student2.inputScores()
    average = student2.calcAvg()
    print("Average score of", student2.name, "is:", average)


main()
