from module import *
from Student import *
from exceptions import *


class IterStudentRepo:

    def __init__(self):
        data = []
        d = IterableStore(data)
        self._studentRepo = iter(d)

    def addStudent(self, s):
        for stud in self._studentRepo:
            if stud.Id == s.Id:
                raise DuplicateId('Duplicate id!')
        self._studentRepo.append(s)

    def findStudent(self, id):
        for s in self._studentRepo:
            if s.Id == id:
                return s

    def removeStudent(self, id):
        for i in range(len(self._studentRepo)):
            if self._studentRepo[i].Id == id:
                del self._studentRepo[i]
                break

    def updateName(self, newName, id):
        s = self.findStudent(id)
        s.Name = newName

    def listStudents(self):
        for s in self._studentRepo:
            print(str(s))

    def __len__(self):
        return len(self._studentRepo)

    def __getitem__(self, i):
        return self._studentRepo[i]

'''
repo = StudentRepo()
repo.addStudent(Student(3,'Andrei'))
repo.addStudent(Student(2,'Rares'))
repo.removeStudent(2)
repo.updateName('Hagi',3)
#print(repo[1].StudentID)
repo.listStudents()
'''