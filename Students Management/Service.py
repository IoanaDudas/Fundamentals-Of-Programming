from Discipline import Discipline
from DisciplineRepo import DisciplineRepo
from Student import Student
from StudentRepo import StudentRepo
from Grade import *
from GradeRepo import *
from TextRepo import *
from BinaryRepo import *
from exceptions import *
import random
from UndoController import *
import pickle
import json
from moduleDisciplineRepo import *
from moduleGradeRepo import *
from moduleStudentRepo import *


def rndS():
    ran = [[1, 'Javier Moro'], [2, 'Dalai Lama'], [3, 'Dan Brown'], [4, 'J. D. Salinger'],
           [5, 'J. R. R. Tolkien'], [6, 'Markus Zusak'], [7, 'Orson Scott Card'], [8, 'Stephenie Meyer'],
           [9, 'Lois Lowry'], [10, 'Paulo Coelho'], [11, 'Homer'], [12, 'C. S. Lewis'],
           [13, 'John Steinbeck'], [14, 'Herman Melville'], [15, 'Terry Pratchett'], [16, 'Sylvia Plath'],
           [17, 'Hermann Hesse'], [18, 'Jane Austen'], [19, 'Dante Alighieri'], [20, 'Diana Gabaldon'],
           [21, 'Jennifer Smith'], [22, 'John Steinbeck'], [23, 'Daniel Defoe'], [24, 'Roald Dahl']]
    l = []
    res = []
    for i in range(10):
        elem = random.choice(ran)
        l.append(elem)
        ran.remove(elem)
    for i in range(10):
        student = Student(l[i][0], l[i][1])
        res.append(student)
    '''f = open('students.pickle', "wb")
    pickle.dump(res, f)
    f.close()'''
    return res


def rndD():
    ran = [[1, 'Algebra'], [2, 'Geometry'], [3, 'Physics'], [4, 'Chemistry'],
           [5, 'Biology'], [6, 'Spanish'], [7, 'French'], [8, 'Calculus'],
           [9, 'World History'], [10, 'Economics'], [11, 'Physical Education'], [12, 'Digital Arts'],
           [13, 'Web Design'], [14, 'English'], [15, 'Geography'], [16, 'Latin'],
           [17, 'Grammar'], [18, 'Journalism'], [19, 'Painting'], [20, 'Astronomy'],
           [21, 'Fundamentals of Programming'], [22, 'CSA'], [23, 'Object-oriented Programming'],
           [24, 'Computational Logic']]
    l = []
    res = []
    for i in range(10):
        elem = random.choice(ran)
        l.append(elem)
        ran.remove(elem)
    for i in range(10):
        discipline = Discipline(l[i][0], l[i][1])
        res.append(discipline)
    '''f = open('disciplines.pickle', "wb")
    pickle.dump(res, f)
    f.close()'''
    return res


def rndG(sList, dList):
    res = []
    for i in range(10):
        s = random.choice(sList)
        d = random.choice(dList)
        value = random.randint(1, 10)
        grade = Grade(d, s, value)
        res.append(grade)
    '''f = open('grades.pickle', "wb")
    pickle.dump(res, f)
    f.close()'''
    return res


class DTO1:
    def __init__(self, student, avg):
        self._student = student
        self._avg = avg

    def __str__(self):
        return 'Student ' + str(self._student) + '\nAggregated average: ' + str(self._avg) + '\n'


class DTO2:
    def __init__(self, discipline, avg):
        self._discipline = discipline
        self._avg = avg

    def __str__(self):
        return 'Discipline ' + str(self._discipline) + '\nAverage grade: ' + str(self._avg) + '\n'


class Service:
    def __init__(self, studentRepo, disciplineRepo, gradeRepo, undoController, inMemory):
        self._undoController = undoController
        self._grade = gradeRepo
        self._student = studentRepo
        self._discipline = disciplineRepo
        if inMemory is True:
            sList = rndS()
            for s in sList:
                self._student.addStudent(s)
            dList = rndD()
            for d in dList:
                self._discipline.addDiscipline(d)
            gList = rndG(sList, dList)
            for g in gList:
                self._grade.addGrade(g)

    def getByIdDiscipline(self, id):
        for each in self._discipline._disciplines:
            if id == each.Id:
                return each

    def getByIdStudent(self, id):
        for each in self._student._students:
            if id == each.Id:
                return each

    def studentsFailing(self):
        res = []
        for student in self._student._students:
            studDict = {}
            for discipline in self._discipline._disciplines:
                studDict[discipline.Id] = 0
            for grade in self._grade._grades:
                if grade.studentId.Id == student.Id:
                    if not (studDict[grade.disciplineId.Id] == 0):
                        studDict[grade.disciplineId.Id] = (studDict[grade.disciplineId.Id] + grade.GradeV) / 2
                    else:
                        studDict[grade.disciplineId.Id] = grade.GradeV
            fail = False
            for each in studDict.keys():
                if studDict[each] < 5 and not (studDict[each] == 0):
                    fail = True
            if fail == True:
                res.append(Student(student.Id, student.Name))
        return res

    def bestStudents(self):
        res = []
        for student in self._student._students:
            studDict = {}
            for discipline in self._discipline._disciplines:
                studDict[discipline.Id] = 0
            for grade in self._grade._grades:
                if grade.studentId.Id == student.Id:
                    if not (studDict[grade.disciplineId.Id] == 0):
                        studDict[grade.disciplineId.Id] = (studDict[grade.disciplineId.Id] + grade.GradeV) / 2
                    else:
                        studDict[grade.disciplineId.Id] = grade.GradeV
            avg = 0
            for each in studDict.keys():
                if not (studDict[each] == 0):
                    if avg == 0:
                        avg = studDict[each]
                    else:
                        avg = (avg + studDict[each]) / 2
            res.append([student.Id, avg])

        def sortSecond(value):
            return value[1]
        res = sorted(res, key=sortSecond, reverse=True)
        final = []
        for result in range(len(res)):
            obj = DTO1(self.getByIdStudent(res[result][0]), res[result][1])
            final.append(obj)
        return final

    def disciplinesGrades(self):
        res = []
        for discipline in self._discipline._disciplines:
            avg = 0
            for grade in self._grade._grades:
                if grade.disciplineId.Id == discipline.Id:
                    if not (avg == 0):
                        avg = (avg + grade.GradeV) / 2
                    else:
                        avg = grade.GradeV
            if not(avg == 0):
                res.append([discipline.Id, avg])

        def sortSecond(value):
            return value[1]
        res = sorted(res, key=sortSecond, reverse=True)
        final = []
        for result in range(len(res)):
            obj = DTO2(self.getByIdDiscipline(res[result][0]), res[result][1])
            final.append(obj)
        return final

    def undo(self):
        self._undoController.undo()

    def redo(self):
        self._undoController.redo()


