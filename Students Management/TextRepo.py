from StudentRepo import *
from Student import *
from DisciplineRepo import *
from Discipline import *
from GradeRepo import *
from Grade import *


class RepoStudentsT(StudentRepo):

    def __init__(self, gradeRepo, undoController, filename):
        StudentRepo.__init__(self, gradeRepo, undoController)
        self._filename = filename
        self._loadFile()

    def _saveFile(self):
        f = open(self._filename, 'w')
        for i in self.getStudents():
            f.write(str(i.Id) + ';' + str(i.Name) + '\n')

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
        f = open(self._filename, 'r')
        f1 = f.readlines()
        for line in f1:
            line = line.split(';')
            student = Student(int(line[0]), line[1])
            self.addStudent(student)


class RepoDisciplinesT(DisciplineRepo):

    def __init__(self, gradeRepo, undoController, filename):
        DisciplineRepo.__init__(self, gradeRepo, undoController)
        self._filename = filename
        self._loadFile()

    '''def store(self,object):
        DisciplineRepo.addDiscipline(self, object)
        self._saveFile()'''

    def _saveFile(self):
        f = open(self._filename, 'w')
        for i in self.getDisciplines():
            f.write(str(i.Id) + ';' + str(i.Name) + '\n')

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
        f = open(self._filename, 'r')
        f1 = f.readlines()
        for line in f1:
            line = line.split(';')
            discipline = Discipline(int(line[0]), line[1])
            self.addDiscipline(discipline)


class RepoGradeT(GradeRepo):

    def __init__(self, undoController, filename):
        GradeRepo.__init__(self, undoController)
        self._filename = filename
        self._loadFile()

    '''def store(self,object):
        GradeRepo.addG(self,object)
        self._saveFile()'''

    def _saveFile(self):
        f = open(self._filename, 'w')
        for i in self.getGrades():
            f.write(str(i.disciplineId.Id) + ';' + str(i.disciplineId.Name) + ';' + str(i.studentId.Id) + ';' + str(i.studentId.Name) + ';' + str(i.GradeV) + '\n')

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
        f = open(self._filename, 'r')
        f1 = f.readlines()
        for line in f1:
            line = line.split(';')
            grade = Grade(Discipline(int(line[0]), line[1]), Student(int(line[2]), line[3]), int(line[4]))
            self.addGrade(grade)

