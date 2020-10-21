from exceptions import *

class Grade:

    def __init__(self, discipline, student, gradeV):
        self._discipline = discipline
        self._student = student
        if gradeV<1 or gradeV>10:
            raise GradeException("Grade must be >0 and <=10!")
        self._gradeV = gradeV

    @property
    def disciplineId(self):
        return self._discipline
    
    @property
    def studentId(self):
        return self._student

    @property
    def GradeV(self):
        return self._gradeV
    
    def __str__(self):
        return 'Discipline '+str(self._discipline)+'\nStudent '+str(self._student)+'\nGrade: '+str(self._gradeV)+'\n'