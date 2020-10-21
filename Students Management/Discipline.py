from exceptions import *

class Discipline:

    def __init__(self, disciplineId, name):
        if disciplineId == None:
            raise IdException("Discipline ID cannot be none")
        if disciplineId < 0:
            raise IdException("Discipline ID cannot be <0!")
        self._id = disciplineId
        if name=='':
            raise NameException("Name cannot be none!")
        self._name = name

    @property
    def Id(self):
        return self._id

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    def __str__(self):
        return 'ID: '+str(self._id)+'\nDiscipline name: '+self._name