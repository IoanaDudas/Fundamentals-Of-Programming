from StudentRepo import *
from Student import *
from DisciplineRepo import *
from Discipline import *
from GradeRepo import *
from Grade import *
import pickle

class RepoStudentsB(StudentRepo):

    def __init__(self, gradeRepo, undoController, filename):
        StudentRepo.__init__(self, gradeRepo, undoController)
        self._filename = filename
        self._loadFromFile()

    def _saveFile(self):
        f = open(self._filename, "wb")
        pickle.dump(self.getStudents(), f)
        f.close()

    '''def store(self, object):
        StudentRepo.addS(self, object)
        self._saveFile()'''

    def addStudent(self, student):
        StudentRepo.addStudent(self, student)
        self._saveFile()

    def removeStudent(self, student):
        StudentRepo.removeStudent(self, student)
        self._saveFile()

    def updateStudent(self, id, newName):
        StudentRepo.updateStudent(self, id, newName)
        self._saveFile()

    def _loadFile(self):
        result = []
        f = open(self._filename, "rb")
        return pickle.load(f)

    def _loadFromFile(self):
        for obj in self._loadFile():
            self.addStudent(obj)


class RepoDisciplinesB(DisciplineRepo):

    def __init__(self, gradeRepo, undoController, filename):
        DisciplineRepo.__init__(self, gradeRepo, undoController)
        self._filename = filename
        self._loadFromFile()

    '''def store(self,object):
        DisciplineRepo.addDiscipline(self, object)
        self._saveFile()'''

    def _saveFile(self):
        f = open(self._filename, "wb")
        pickle.dump(self.getDisciplines(), f)
        f.close()

    def addDiscipline(self, discipline):
        DisciplineRepo.addDiscipline(self, discipline)
        self._saveFile()

    def removeDiscipline(self, discipline):
        DisciplineRepo.removeDiscipline(self, discipline)
        self._saveFile()

    def updateDiscipline(self, id, newName):
        DisciplineRepo.updateDiscipline(self, id, newName)
        self._saveFile()

    def _loadFile(self):
        result = []
        f = open(self._filename, "rb")
        return pickle.load(f)

    def _loadFromFile(self):
        for obj in self._loadFile():
            self.addDiscipline(obj)


class RepoGradeB(GradeRepo):

    def __init__(self, undoController, filename):
        GradeRepo.__init__(self, undoController)
        self._filename = filename
        self._loadFromFile()

    '''def store(self,object):
        GradeRepo.addG(self,object)
        self._saveFile()'''

    def _saveFile(self):
        f = open(self._filename, "wb")
        pickle.dump(self.getGrades(), f)
        f.close()

    def addGrade(self, grade):
        GradeRepo.addGrade(self, grade)
        self._saveFile()

    '''def deleteGS(self,id):
        GradeRep.deleteGS(self,id)
        self._saveFile()
        
    def deleteGA(self,id):
        GradeRep.deleteGA(self,id)
        self._saveFile()
        
    def gradestud(self,ids,ida,grade):
        GradeRep.gradestud(self,ids,ida,grade)
        self._saveFile()'''

    def _loadFile(self):
        f = open(self._filename, "rb")
        return pickle.load(f)

    def _loadFromFile(self):
        for obj in self._loadFile():
            self.addGrade(obj)

