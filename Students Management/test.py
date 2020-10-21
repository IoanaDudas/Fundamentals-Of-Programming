from Discipline import Discipline
from DisciplineRepo import DisciplineRepo
from Student import Student
from StudentRepo import StudentRepo
from DisciplineRepo import DisciplineRepo
from Grade import Grade
from GradeRepo import GradeRepo
from UndoController import *
from Service import *
from exceptions import *
import random
from copy import deepcopy
import unittest

def rndS():
    ran = [[1, 'Javier Moro'], [2, 'Dalai Lama'], [3, 'Dan Brown'], [4, 'J. D. Salinger'],
           [5, 'J. R. R. Tolkien'], [6, 'Markus Zusak'], [7, 'Orson Scott Card'], [8, 'Stephenie Meyer'],
           [9, 'Lois Lowry'], [10, 'Paulo Coelho']]
    res = []
    for i in range(10):
        student = Student(ran[i][0], ran[i][1])
        res.append(student)
    return res


def rndD():
    ran = [[1, 'Algebra'], [2, 'Geometry'], [3, 'Physics'], [4, 'Chemistry'],
           [5, 'Biology'], [6, 'Spanish'], [7, 'French'], [8, 'Calculus'],
           [9, 'World History'], [10, 'Economics']]
    res = []
    for i in range(10):
        discipline = Discipline(ran[i][0], ran[i][1])
        res.append(discipline)
    return res


def rndG(sList, dList):
    res = []
    for i in range(10):
        s = sList[i]
        d = dList[i]
        value = random.randint(1, 10)
        grade = Grade(d, s, value)
        res.append(grade)
    return res

class test(unittest.TestCase):

    def setUp(self):
        self._service = Service()
        self._undoController = UndoController()
        self._grade = GradeRepo(self._undoController)
        self._student = StudentRepo(self._grade, self._undoController)
        self._discipline = DisciplineRepo(self._grade, self._undoController)
        sList = rndS()
        for s in sList:
            self._student.addStudent(s)
        dList = rndD()
        for d in dList:
            self._discipline.addDiscipline(d)
        gList = rndG(sList, dList)
        for g in gList:
            self._grade.addGrade(g)

    def testStudent(self):
        self.assertRaises(IdException, Student, None, 'name')
        self.assertRaises(IdException, Student, -2, 'name')
        self.assertRaises(NameException, Student, 11, '')
        student = Student(11, 'name')

    def testDiscipline(self):
        self.assertRaises(IdException, Discipline, None, 'name')
        self.assertRaises(IdException, Discipline, -2, 'name')
        self.assertRaises(NameException, Discipline, 11, '')
        discipline = Discipline(11, 'name')

    def testGrade(self):
        student = Student(11, 'name')
        discipline = Discipline(11, 'name')
        self.assertRaises(GradeException, Grade, discipline, student, 11)
        grade = Grade(discipline, student, 10)
        self.assertEqual(grade.GradeV, 10)

    def testUndo(self):
        for i in range(30):
            self._undoController.undo()
        self.assertRaises(DoException, self._undoController.undo)
        for i in range(30):
            self._undoController.redo()
        self.assertRaises(DoException, self._undoController.redo)
        for i in range(30):
            self._undoController.undo()
        student = Student(70, 'Alex')
        self._student.addStudent(student)
        self.assertRaises(DoException, self._undoController.redo)


    def testInit(self):
        self._student.__init__(self._grade, self._undoController)
        self.assertEqual(len(self._student._students), 0)
        self.assertEqual(self._student._gradeRepo, self._grade)
        self.assertEqual(self._student._undoController, self._undoController)

    def testAddStudent(self):
        student = Student(70, 'Alex')
        self._student.addStudent(student)
        self.assertEqual(len(self._student._students), 11)
        student = Student(70, 'Alex')
        self.assertRaises(IdException, self._student.addStudent, student)
        self._student.removeStudent(student)
        self.assertEqual(self._grade.findGrades(student, None), None)
        self.assertRaises(GradeException, self._grade.removeGrades,student.Id, None)
        
    def testRemoveStudent(self):
        s = Student(1, 'Javier Moro')
        self._student.removeStudent(s)
        self.assertEqual(len(self._student._students), 9)
        s = Student(20, 'Alex')
        self.assertRaises(IdException, self._student.removeStudent, s)
        self._undoController.undo()
        self.assertEqual(len(self._student._students), 10)
        self._undoController.redo()
        self.assertEqual(len(self._student._students), 9)
    
    def testUpdateStudent(self):
        s = Student(70, 'Alex')
        self._student.addStudent(s)
        self._student.updateStudent(70, 'John')
        self.assertEqual(s.Name, 'John')
        self.assertRaises(IdException, self._student.updateStudent, 20, 'Alex')
        self.assertRaises(NameException, self._student.updateStudent, 70, 'John')

    def testPrintStudents(self):
        students = deepcopy(self._student.printStudents())
        self.assertNotEqual(self._student._students, students)

    def testGetStudents(self):
        students = self._student.getStudents()
        self.assertEqual(self._student._students, students)

    def testSearchStudentsName(self):
        self.assertEqual(len(self._student.searchStudentsName('j')), 3)

    def testSearchStudentsId(self):
        self.assertEqual(len(self._student.searchStudentsId(1)), 1)

    def testAddDiscipline(self):
        discipline = Discipline(34, 'Math')
        self._discipline.addDiscipline(discipline)
        self.assertEqual(len(self._discipline._disciplines), 11)
        discipline = Discipline(34, 'Math')
        self.assertRaises(IdException, self._discipline.addDiscipline, discipline)
    
    def testRemoveDiscipline(self):
        discipline = Discipline(10, 'Economics')
        self._discipline.removeDiscipline(discipline)
        self.assertEqual(len(self._discipline._disciplines), 9)
        discipline = Discipline(34, 'Math')
        self.assertRaises(IdException, self._discipline.removeDiscipline, discipline)
    
    def testUpdateDiscipline(self):
        discipline = Discipline(34, 'Math')
        self._discipline.addDiscipline(discipline)
        self._discipline.updateDiscipline(34, 'English')
        self.assertEqual(discipline.Name, 'English')
        self.assertRaises(IdException, self._discipline.updateDiscipline, 20, 'Math')
        self.assertRaises(NameException, self._discipline.updateDiscipline, 34, 'English')

    def testPrintDisciplines(self):
        disciplines = deepcopy(self._discipline.printDisciplines())
        self.assertNotEqual(self._discipline._disciplines, disciplines)

    def testGetDisciplines(self):
        disciplines = self._discipline.getDisciplines()
        self.assertEqual(self._discipline._disciplines, disciplines)

    def testSearchDisciplinesName(self):
        self.assertEqual(len(self._discipline.searchDisciplinesName('h')), 5)

    def testSearchDisciplinesId(self):
        self.assertEqual(len(self._discipline.searchDisciplinesId(1)), 1)

    def testPrintGrades(self):
        grades = deepcopy(self._grade.printGrades())
        self.assertNotEqual(self._grade._grades, grades)

    def testGetGrades(self):
        grades = self._grade.getGrades()
        self.assertEqual(self._grade._grades, grades)

    def testAddGradeValidation(self):
        student = Student(70, 'Alex')
        self._student.addStudent(student)
        discipline = Discipline(34, 'Math')
        self._discipline.addDiscipline(discipline)
        grade = Grade(discipline, student, 8)
        self.assertRaises(GradeException, self._grade.addGradeValidation, grade)
        discipline = Discipline(2, 'Geometry')
        grade = Grade(discipline, student, 8)
        self.assertRaises(GradeException, self._grade.addGradeValidation, grade)
        student = Student(1, 'Javier Moro')
        discipline = Discipline(34, 'Math')
        grade = Grade(discipline, student, 8)
        self.assertRaises(GradeException, self._grade.addGradeValidation, grade)
        student = Student(1, 'Javier Moro')
        discipline = Discipline(10, 'Economics')
        grade = Grade(discipline, student, 8)
        self._grade.addGradeValidation(grade)
        self.assertEqual(len(self._grade._grades), 11)

    '''def testGetByIdDiscipline(self):
        discipline = Discipline(90, 'name')
        self._discipline.addDiscipline(discipline)
        self.assertNotEqual(self._service.getByIdDiscipline(90), None)

    def testGetByIdStudent(self):
        student = Student(90, 'name')
        self._student.addStudent(student)
        self.assertNotEqual(self._service.getByIdStudent(90), None)'''

    def testBestStudents(self):
        self.assertNotEqual(self._service.bestStudents(), [])

    def testDisciplinesGrades(self):
        self.assertNotEqual(self._service.disciplinesGrades(), [])

    def testStudentsFailing(self):
        self.assertNotEqual(self._service.studentsFailing(), [])

if __name__ == '__main__':
    unittest.main()
