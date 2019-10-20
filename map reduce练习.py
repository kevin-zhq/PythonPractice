# 将列表内的字符串格式化成大写字母开头其余小写的格式
def normalize(name):
    return name.lower().capitalize()

l1 = ['adam','LISA','barT']
l2 = list(map(normalize,l1))
print(l2)

l3 = [x.lower().capitalize() for x in l1 ]
print(l3)

l4 = list(map(lambda x : x.lower().capitalize(),l1))
print(l4)

#编写一个列表内数字求积的函数
from functools import reduce
def prod(a,b):
    return a*b
l5 = [3,5,7,9]
c = reduce(prod,l5)
print('乘积等于%d' % c)
# print(reduce(lambda x,y : x*y,l5))

#将字符串类型的数字转换成浮点数
def str2float(s):
    # char2int
    def g(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    # 整数部分
    def h(x,y):
        return 10*x + y
    # 小数部分
    def a(x,y):
        return x/10 + y
 
    # 将原始字符串数据分割为两部分
    if '.' in s:
        L = s.split('.')
        q = list(map(g,L[0]))
        u = list(map(g,L[1]))
        b = u[::-1]      #从最低位到十分位排序
        return reduce(h,q) + reduce(a,b)/10
    else:
        return reduce(h,map(g,s))


print (str2float('123.789456'))
print (str2float('123789456'))


