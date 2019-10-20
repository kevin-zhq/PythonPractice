class Student(object):
    __slots__ = ('name','age')      #只能对当前类起作用，对继承类无效，除非继续定义__slots__

a = Student()
a.name = 'ZhangPeining'
# b.class2 = 2      弹出错误，属于未指定的属性名称
a.age = 7
print(a.name,a.age)