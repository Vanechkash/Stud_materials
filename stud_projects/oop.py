class Cat:
    def __init__(self, name):
        self.name = name
        self.__liver__ = 50

    @property
    def liver(self):  # выводит значение
        print('property')
        return self.__liver__

    @liver.setter
    def liver(self, newliver):  # вносит изменения
        print('setter')
        if type(newliver) in [int, float] and 300 > newliver > 20:
            self.__liver__ = newliver

    def method_age(self):
        self.age = 3
        self.__method_close__()

    def __method_close__(self):
        print('closed')


c = Cat("Jarry")
c.name
c1 = Cat('Tom')
c1.method_age()

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.r = None
        self.l = None


class Tree:
    def __init__(self, root):
        self.root = root

    def add(self, newstudent):
        cur = self.root
        while True:
            if newstudent.score > cur.score:  # r
                if cur.r:
                    cur = cur.r
                else:
                    cur.r = newstudent
                    break
            else:  # l
                if cur.l:
                    cur = cur.l
                else:
                    cur.l = newstudent
                    break

root = Student('Boris', 6)
tree = Tree(root)

tree.add(Student('Egor', 6.5))
tree.add(Student('Pavel', 5))
tree.add(Student('Sergey', 6.6))
tree.add(Student('Vlad', 6.4))
tree.add(Student('Gena', 6.4))

root.r.r.name


def print_tree(root):
    print(root.name, root.score)
    if root.r:
        print_tree(root.r)
    if root.l:
        print_tree(root.l)

print_tree(root)