# __slots__ 选定当前类的属性名称
# __len__()方法作用于len()函数

'''
#__str__()方法定义 类变量的显示字符串
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

am = Student('Michale')
print(am)

#但是不能直接交互显示变量 am，而不用print方法，直接调用变量名称用 __repr__()方法
'''

'''
#__iter__() 方法返回一个可迭代对象

class Fib(object):
    def __init__(self):
        self.a , self.b = 0 , 1
    def __iter__(self):
        return self             #实例本身就是可迭代对象，故返回本身

    def __next__(self):
        self.a , self.b = self.b , self.a + self.b
        if self.a > 1000:                #设定循环退出的条件
            raise StopIteration();
        return self.a

for n in Fib():
    print(n)
'''

