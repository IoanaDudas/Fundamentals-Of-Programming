from Service import *
from exceptions import *

class ui:
    def __init__(self, service):
        self._service = service
        self._student = self._service._student
        self._discipline = self._service._discipline
        self._grade = self._service._grade


    def menu(self):
        while True:
            print('1. Add student')
            print('2. Remove student')
            print('3. Update student')
            print('4. Show the list of students')
            print('5. Add discipline')
            print('6. Remove discipline')
            print('7. Update discipline')
            print('8. Show the list of disciplines')
            print('9. Add grade')
            print('10. Show the list of grades')
            print('11. Search students')
            print('12. Search students')
            print('13. Students failing')
            print('14. Students with the best grades')
            print('15. Disciplines sorted')
            print('16. Undo')
            print('17. Redo')
            print('18. Exit')

            try:
                try:
                    choice=int(input("-> "))
                except:
                    raise IntException("Invalid option!")
                print('')
                if choice == 1:
                    self.addStudent()
                    print('')
                elif choice == 2:
                    self.removeStudent() 
                    print('')
                elif choice == 3:
                    self.updateStudent() 
                    print('') 
                elif choice == 4:
                    self.listStudents()
                    print('')
                elif choice == 5:
                    self.addDiscipline()
                    print('')
                elif choice == 6:
                    self.removeDiscipline() 
                    print('')
                elif choice == 7:
                    self.updateDiscipline() 
                    print('') 
                elif choice == 8:
                    self.listDisciplines()
                    print('')
                elif choice == 9:
                    self.addGrade()
                    print('')
                elif choice == 10:
                    self.listGrades()
                    print('')
                elif choice == 11:
                    self.searchStudents()
                    print('')
                elif choice == 12:
                    self.searchDiscipline()
                    print('')
                elif choice == 13:
                    self.statistic1()
                    print('')
                elif choice == 14:
                    self.statistics2()
                    print('')
                elif choice == 15:
                    self.statistics3()
                    print('')
                elif choice == 16:
                    self.undo()
                    print('')
                elif choice == 17:
                    self.redo()
                    print('')
                elif choice == 18:
                    break
                else:
                    raise IntException("Invalid option!")
            except Exception as msg:
                print(msg, '\n')

    def addStudent(self):
        try:
            try:
                id = int(input('student Id: '))
            except:
                raise IdException("Student ID must be int!")
            name = input("Student's name: ")
            student = Student(id, name)
            self._student.addStudent(student)
        except Exception as msg:
            print(msg, '\n')

    def removeStudent(self):
        try:
            try:
                id = int(input('student Id: '))
            except:
                raise IdException("Student ID must be int!")
            student = Student(id, 'name')
            self._student.removeStudent(student)
        except Exception as Msg:
            print(Msg, '\n')

    def updateStudent(self):
        try:
            try:
                id = int(input('student Id: '))
            except:
                raise IdException("Student ID must be int!")
            newName = input("Student's new name: ")
            self._student.updateStudent(id, newName)
        except Exception as msg:
            print(msg, '\n')

    def listStudents(self):
        students = self._student.getStudents()
        for i in students:
            print(i)
        print('')

    def addDiscipline(self):
        try:
            try:
                id = int(input('discipline Id: '))
            except:
                raise IdException("Discipline ID must be int!")
            name = input("Discipline's name: ")
            discipline = Discipline(id, name)
            self._discipline.addDiscipline(discipline)
        except Exception as msg:
            print(msg, '\n')

    def removeDiscipline(self):
        try:
            try:
                id = int(input('discipline Id: '))
            except:
                raise IdException("Discipline ID must be int!")
            discipline = Discipline(id, 'name')
            self._discipline.removeDiscipline(discipline)
        except Exception as msg:
            print(msg, '\n')        
        
    def updateDiscipline(self):
        try:
            try:
                id = int(input('discipline Id: '))
            except:
                raise IdException("Discipline ID must be int!")
            newName = input("Discipline's new name: ")
            self._discipline.updateDiscipline(id, newName)
        except Exception as msg:
            print(msg, '\n')

    def listDisciplines(self):
        disciplines = self._discipline.getDisciplines()
        for i in disciplines:
            print(i)
        print('')

    def addGrade(self):
        try:
            try:
                dId = int(input('discipline Id: '))
            except:
                raise IdException("Discipline ID must be int!")
            try:
                sId = int(input('students Id: '))
            except:
                raise IdException("Student ID must be int!")
            try:
                value = int(input('grade: '))
            except:
                raise IdException("Grade must be int!")
            discipline = self._service.getByIdDiscipline(dId)
            student = self._service.getByIdStudent(sId)
            grade = Grade(discipline, student, value)
            self._grade.addGradeValidation(grade)
        except Exception as msg:
            print(msg, '\n')
    
    def listGrades(self):
        grades = self._grade.getGrades()
        for i in grades:
            print(i)
        print('')

    def searchStudents(self):
        try:
            s = input('Search students by: ')
            try:
                sId = int(s)
                students = self._student.searchStudentsId(sId)
            except:
                students = self._student.searchStudentsName(s)
            if students == []:
                raise GradeException("Students don't exist !")
            for each in students:
                print(each)
        except Exception as msg:
            print(msg, '\n')

    def searchDiscipline(self):
        try:
            d = input('Search disciplines by: ')
            try:
                dId = int(d)
                disciplines = self._discipline.searchDisciplinesName(dId)
            except:
                disciplines = self._discipline.searchDisciplinesName(d)
            if disciplines == []:
                raise GradeException("Disciplines don't exist !")
            for each in disciplines:
                print(each)
        except Exception as msg:
            print(msg, '\n')

    def statistic1(self):
        fail = self._service.studentsFailing()
        for each in fail:
            print(each)

    def statistics2(self):
        best = self._service.bestStudents()
        for each in best:
            print(each)

    def statistics3(self):
        dis = self._service.disciplinesGrades()
        for each in dis:
            print(each)

    def undo(self):
        try:
            self._service.undo()
        except Exception as msg:
            print(msg, '\n')

    def redo(self):
        try:
            self._service.redo()
        except Exception as msg:
            print(msg, '\n')

'''
if __name__=='__main__':
    current_ui = ui()
    current_ui.menu()
'''