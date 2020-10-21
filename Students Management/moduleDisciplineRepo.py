from module import *
from Discipline import *
from exceptions import *


class IterDisciplineRepo:

    def __init__(self):
        data = []
        d = IterableStore(data)
        self._disciplineRepo = iter(d)


    def addDiscipline(self, d):
        for discipline in self._disciplineRepo:
            if discipline.Id == d.Id:
                raise DuplicateId('Duplicate id!')
        self._disciplineRepo.append(d)

    def findDiscipline(self, id):
        for d in self._disciplineRepo:
            if d.Id == id:
                return d

    def removeDiscipline(self,id):
        for i in range(len(self._disciplineRepo)):
            if self._disciplineRepo[i].Id == id:
                del self._disciplineRepo[i]
                break

    def updateName(self, newName, id):
        d = self.findDiscipline(id)
        d.Name = newName

    def listDiscipline(self): #prints all assignments in the list
        for a in self._disciplineRepo:
            print(str(a))

    def __len__(self):
        return len(self._disciplineRepo)

    def __getitem__(self, i):
        return self._disciplineRepo[i]

'''
repo = DisciplineRepo()
repo.addDiscipline(Discipline(3,'Andrei'))
repo.addDiscipline(Discipline(2,'Rares'))
repo.removeDiscipline(2)
repo.updateName('Hagi',3)
#print(repo[1].StudentID)
repo.listDiscipline()
'''