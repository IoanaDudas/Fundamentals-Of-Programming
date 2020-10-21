from Student import *
from copy import deepcopy
from exceptions import *
import re
from UndoController import FunctionCall, Operation, CascadedOperation, UndoController
from GradeRepo import *


class StudentRepo:

    def __init__(self, GradeRepo, UndoController):
        self._students = []
        self._gradeRepo = GradeRepo
        self._undoController = UndoController

    def addStudent(self, student):
        for s in self._students:
            if s.Id == student.Id:
                raise IdException("Student ID already exists!")
        self._students.append(student)
        undo = FunctionCall(self.removeStudent, student)
        redo = FunctionCall(self.addStudent, student)
        op = Operation(undo, redo)
        self._undoController.recordOperation(op)
        return student

    def removeStudent(self, student):
        ok = 1
        for s in self._students:
            if s.Id == student.Id:
                student = s
                self._students.remove(s)
                ok = 0
        if ok == 1:
            raise IdException("Student ID doesn't exist!")
        undo = FunctionCall(self.addStudent, student)
        redo = FunctionCall(self.removeStudent, student)
        op = CascadedOperation(Operation(undo, redo))
        grades = self._gradeRepo.filterGrades(student, None)
        for grade in grades:
            self._gradeRepo.removeGrades(student.Id, None, True)
            obj = self._undoController.pop()
            op.add(obj)
        self._undoController.recordOperation(op)
        return student

    def updateStudent(self, id, newName):
        ok = 1
        for s in self._students:
            if s.Id == id:
                if s.Name == newName:
                    raise NameException("New name equal to old name!")
                student = deepcopy(s)
                s.Name = newName
                ok = 0
        if ok ==1:
            raise IdException("Student ID doesn't exist!")
        undo = FunctionCall(self.updateStudent, student.Id, student.Name)
        redo = FunctionCall(self.updateStudent, student.Id, newName)
        op = Operation(undo, redo)
        self._undoController.recordOperation(op)
        return student

    def printStudents(self):
        return deepcopy(self._students)
    
    def getStudents(self):
        return self._students

    def searchStudentsName(self, param):
        res = []
        for s in self._students:
            aux = s.Name
            match = re.search(param.lower(), aux.lower())
            if match is not None:
                res.append(s)
        return res

    def searchStudentsId(self, param):
        res = []
        for s in self._students:
            if s.Id == param:
                res.append(s)
        return res

