
class IterableStore:
    def __init__(self, data):
        self._data = []
        self._data = data

    def __iter__(self):
        self._currentItem = 0
        return self

    def __next__(self):
        if self._currentItem < len(self._data):
            result = self._data[self._currentItem]
            self._currentItem += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        self._data.remove(self._data[index])

    def remove(self, index):
        self._data.remove(self._data[index])

    def append(self, obj):
        self._data.append(obj)

    def __len__(self):
        return len(self._data)


def sortStudentID(student1, student2):
    if student1.StudentID < student2.StudentID:
        return True
    return False


def sortDisciplineID(discipline1, discipline2):
    if discipline1.DisciplineID < discipline2.DisciplineID:
        return True
    return False


def stupidSort(rez, comp):  # or gnomeSort
    index = 0
    n = len(rez)
    while index < n:
        if index == 0:
            index += 1
        if comp(rez[index], rez[index-1]) == False:
            index += 1
        else:
            rez[index], rez[index-1] = rez[index-1], rez[index]
            index -= 1
    return rez


def fail(x):
    if x.GradeValue < 5:
        return True
    return False


def fillter(rez, function):
    rez2 = []
    for i in range(len(rez)):
        if function(rez[i]) == True:
            rez2.append(rez[i])
    return rez2

'''
def shellSort(data, sym):
    n = len(data)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            res = data[i]
            j = i
            while j >= gap and data[j - gap] > res:
                data[j] = data[j - gap]
                j -= gap
            data[j] = res
        gap //= 2
    return data
    '''



