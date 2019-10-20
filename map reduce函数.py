def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,abs)) #将f变量指向abs函数，通过调用，实现高阶函数

r = map(abs,[-1,-2,-3,-4])      #map函数，第一个参数是函数，第二个参数是可迭代对象；返回一个可迭代对象
print(r)
print(list(r))

from functools import reduce       #reduce函数，第一个参数是函数，第二个参数是可迭代对象；返回的值作为可迭代对象的第一个值，直到最后
def fu(x,y):
    return x*10+y
ad = reduce(fu,[-1,-3,-5,-7,-9])
print(ad)

#将字符串的数字转换成int类型
num = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2num(s):
    def char2num(s):
        return num[s]
    #def fu(x,y):
        #return x*10+y
    # return reduce(fu,map(char2num,s))
    return reduce(lambda x,y: x*10+y,map(char2num,s))       #以上用lambda函数简写

print(str2num('45646'))
