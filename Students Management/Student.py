from exceptions import *

class Student:

    def __init__(self, studentId, name):
        if studentId == None:
            raise IdException("Student ID cannot be none!")
        if studentId < 0:
            raise IdException("Student ID cannot be <0!")
        self._id = studentId
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
        return 'ID: '+str(self._id)+'\nStudent name: '+self._name