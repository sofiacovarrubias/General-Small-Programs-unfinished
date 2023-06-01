import numpy as np


class Grade():

    def __init__(self):
        self.scores = np.zeros(4)
        self.percentages = np.zeros(4)
        self.Grade = None

    def add_scores(self, score_input, percent_input, n):
        #score_input (str): str of scores seperated by a comma
        #percent_input (int): percentage worth of grade
        #n (int): which process to do

        scores_arr = np.array(list(map(int,(score_input).split(','))))
        scores_avg = np.sum(scores_arr)/len(scores_arr)

        if n == 1:
            self.scores[0] = scores_avg
            self.percentages[0] = percent_input
            
        elif n == 3:
            self.scores[1] = scores_avg
            self.percentages[1] = percent_input

        elif n == 5:
            self.scores[2] = scores_avg
            self.percentages[2] = percent_input

        elif n == 7:
            self.scores[3] = scores_avg
            self.percentages[3] = percent_input

            


    def calc_grade(self):
        ratio = self.percentages/np.sum(self.percentages)
        Final_Grade = np.sum(self.scores*ratio)
        return Final_Grade

"""
#TESTING AREA

my_grade = Grade()

homework = '0,100'
quizzes = '0,100,100'
exams = '60,100'
final_exam = '80'

my_grade.add_scores(homework, 21, 1)
my_grade.add_scores(quizzes, 18, 3)
my_grade.add_scores(exams, 45, 5)
my_grade.add_scores(final_exam, 16, 7)

my_grade.calc_grade()

"""