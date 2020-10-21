from Grade import *
from copy import deepcopy
from exceptions import *
from Discipline import *
from Student import *
from UndoController import FunctionCall, Operation, CascadedOperation, UndoController


class GradeRepo:
    def __init__(self, UndoController):
        self._grades = []
        self._undoController = UndoController
    
    def addGradeValidation(self, grade):
        okD = 0
        okS = 0
        for g in self._grades:
            if grade.disciplineId.Id == g.disciplineId.Id:
                okD = 1
            if grade.studentId.Id == g.studentId.Id:
                okS = 1
        if okD == 0 and okS == 0:
            raise GradeException("Discipline and student don't exist!")
        elif okS == 0:
            raise GradeException("Student doesn't exist!")
        elif okD == 0:
            raise GradeException("Discipline doesn't exist!")
        self._grades.append(grade)
        undo = FunctionCall(self.removeGrades, grade.studentId.Id, None)
        redo = FunctionCall(self.addGrade, grade)
        op = Operation(undo, redo)
        self._undoController.recordOperation(op)
        return grade

    def filterGrades(self, student, discipline):
        res = []
        for grade in self._grades:
            if student is not None and grade.studentId != student:
                continue
            if discipline is not None and grade.disciplineId != discipline:
                continue
            res.append(grade)
        return res

    def addGrade(self, grade):
        self._grades.append(grade)
        undo = FunctionCall(self.removeGrades, grade.studentId.Id, None)
        redo = FunctionCall(self.addGrade, grade)
        op = Operation(undo, redo)
        self._undoController.recordOperation(op)
        return grade

    def printGrades(self):
        return deepcopy(self._grades)
    
    def getGrades(self):
        return self._grades

    def findGrades(self, studentId, disciplineId):
        for grade in self._grades:
            if studentId == None:
                if disciplineId == grade.disciplineId.Id:
                    return grade
            elif disciplineId == None:
                if studentId == grade.studentId.Id:
                    return grade
        return None

    def removeGrades(self, studentId, disciplineId, recordUndo=True):
        grade = self.findGrades(studentId, disciplineId)
        if grade == None:
            raise GradeException("Grade doesn't exist in list!")
        self._grades.remove(grade)
        if recordUndo == True:
            redo = FunctionCall(self.removeGrades, studentId, disciplineId)
            undo = FunctionCall(self.addGrade, grade)
            op = Operation(undo, None)
            self._undoController.recordOperation(op)
        return grade

