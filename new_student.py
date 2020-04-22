#  using getters for private instance variables and setters to change value
#  in private instance variable __final


class Student:

    def __init__(self, student_name):

        """ constructor of class Student """

        self.__name = student_name
        self.__project = 0.0
        self.__midterm = 0.0
        self.__final = 0.0

    def inputScores(self):

        """ input scores from user """

        self.__project = float(input("Enter project score: "))
        self.__midterm = float(input("Enter midterm score: "))
        self.__final = float(input("Enter final score: "))

    def calcAvg(self):

        avg = (self.__project + self.__midterm + self.__final)/3
        return avg

    #  in order to access these outside the class must use getters

    def getMidterm(self):
        return self.__midterm

    def getFinal(self):
        return self.__final

    #  to change variable in private instance use setter
    def setFinal(self, final_score):
        #  to limit final score between 0 and 100 points
        if final_score < 0:
            final_score = 0
        elif final_score > 100:
            final_score = 100
        self.__final = final_score






