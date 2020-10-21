from Discipline import *
from UndoController import FunctionCall, Operation, CascadedOperation
from copy import deepcopy
from exceptions import *
import re
from GradeRepo import *


class DisciplineRepo:

    def __init__(self, GradeRepo, UndoController):
        self._disciplines = []
        self._gradeRepo = GradeRepo
        self._undoController = UndoController
    
    def addDiscipline(self, discipline):
        for d in self._disciplines:
            if d.Id == discipline.Id:
                raise IdException("Discipline ID already exists!")
        self._disciplines.append(discipline)
        undo = FunctionCall(self.removeDiscipline, discipline)
        redo = FunctionCall(self.addDiscipline, discipline)
        op = Operation(undo, redo)
        self._undoController.recordOperation(op)
        return discipline

    def removeDiscipline(self, discipline):
        ok = 1
        for d in self._disciplines:
            if d.Id == discipline.Id:
                discipline = d
                self._disciplines.remove(d)
                ok = 0
        if ok == 1:
            raise IdException("Discipline ID doesn't exist!")
        undo = FunctionCall(self.addDiscipline, discipline)
        redo = FunctionCall(self.removeDiscipline, discipline)
        op = CascadedOperation(Operation(undo, redo))
        grades = self._gradeRepo.filterGrades(None, discipline)
        for grade in grades:
            self._gradeRepo.removeGrades(None, discipline.Id, True)
            obj = self._undoController.pop()
            op.add(obj)
        self._undoController.recordOperation(op)
        return discipline

    def updateDiscipline(self, id, newName):
        ok = 1
        for d in self._disciplines:
            if d.Id == id:
                if d.Name == newName:
                    raise NameException("New name equal to old name!")
                discipline = deepcopy(d)
                d.Name = newName
                ok = 0
        if ok == 1:
            raise IdException("Discipline ID doesn't exist!")
        undo = FunctionCall(self.updateDiscipline, discipline.Id, discipline.Name)
        redo = FunctionCall(self.updateDiscipline, discipline.Id, newName)
        op = Operation(undo, redo)
        self._undoController.recordOperation(op)
        return discipline

    def printDisciplines(self):
        return deepcopy(self._disciplines)
    
    def getDisciplines(self):
        return self._disciplines

    def searchDisciplinesName(self, param):
        res = []
        for d in self._disciplines:
            aux = d.Name
            match = re.search(param.lower(), aux.lower())
            if match is not None:
                res.append(d)
        return res

    def searchDisciplinesId(self, param):
        res = []
        for d in self._disciplines:
            if d.Id == param:
                res.append(d)
        return res