from module import *
from Grade import *


class IterGradeRepo:

    def __init__(self):
        data = []
        d = IterableStore(data)
        self._gradeRepo = iter(d)

    def addGrade(self, g):
        self._gradeRepo.append(g)

    def listGrades(self):
        for g in self._gradeRepo:
            print(str(g))

    def removeStudent(self, studentId):
        i = 0
        n = len(self._gradeRepo)
        while i < n:
            if self._gradeRepo[i].studentId == studentId:
                del self._gradeRepo[i]
                n = n - 1
            else:
                i = i + 1

    def removeDiscipline(self, disciplineId):
        i = 0
        n = len(self._gradeRepo)
        while i < n:
            if self._gradeRepo[i].disciplineId == disciplineId:
                del self._gradeRepo[i]
                n = n - 1
                i = i - 1
            i = i + 1

    def removeGrade(self, studentId, disciplineId):
        i = 0
        n = len(self._gradeRepo)
        while i < n:
            if self._gradeRepo[i].studentId == studentId and self._gradeRepo[i].disciplineId == disciplineId:
                del self._gradeRepo[i]
                break

    def __len__(self):
        return len(self._gradeRepo)

    def __getitem__(self, i):
        return self._gradeRepo[i]

'''
repo = IterGradeRepo()
repo.addGrade(Grade(1, 2, 10))
repo.addGrade(Grade(2, 3, 2))
repo.addGrade(Grade(3, 4, 4))
repo.removeDiscipline(1)
repo.removeStudent(3)
repo.listGrades()
'''