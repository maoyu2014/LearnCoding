class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda:25
        raise AttributeError('Student object has no attribute %s' % attr)


s = Student()
print(s.name)
print(s.score)
print(s.age())
# print(s.grade)

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        if path=='users':
            return lambda name: Chain('%s/%s/:%s' % (self._path, path, name))
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().users('maoyu').repos)
