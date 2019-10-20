#for循环创建质数
'''
for i in range(2,100):
    for j in range(2,i):
        if i%j == 0:
            #print(i,'等于',j,'*',i//j)
            break
    else:
        print(i,'是质数')
        '''

#for循环打印乘法口诀表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(j,i,i*j),end=' ')         #    %d 整数占位符；%s 字符串占位符 %f 浮点数占位符 等等
    print()
'''

#列表解析创建列表[[]],如果创建元组用(())/以及列表解析创建生成器()
'''
biao_ge1 = [[j,i,i*j] for i in range(1,10) for j in range(1,i+1)]
print(biao_ge1)
biao_ge2 = ([j,i,i*j] for i in range(1,10) for j in range(1,i+1))
print(biao_ge2)
biao_ge3 = (i for i in range(1,10) if i%2 ==0)
print(biao_ge3,'加起来总共是：',sum(biao_ge3))
biao_ge3 = [i for i in range(1,10) if i%2 ==0]
print(biao_ge3,'加起来总共是：',sum(biao_ge3))
'''

#字典妙用 四则运算,但是目前好像是能输入整数，不输入或输入其他则报错
'''
while True:
    x = int(input('请输入一个数字：'))
    o = input('请输入+|-|*|/|其中一个运算符号：')
    y = int(input('请输入一个数字：'))
    yun_suan = {'+':x+y,
                '-':x-y,
                '*':x*y,
                '/':x/y
                }
    result = yun_suan.get(o,'请输入正确的运算符号：')
    print(result)
    ji_xu = input('结束请输入：q | 继续请按回车')
    if ji_xu == 'q':
        break
'''

#集合set
'''
x = set('hello')
y = set('world')
a = x&y     #交集
b = x|y     #合集
c = x-y     #x和y组成全集，并求y的补集
d = y-x     #x和y组成全集，并求x的补集
print(a,b,c,d)
'''

class Human:
    name = 'rr'
    gender = 'yy'
    age = '77'
    __money = 8000      #私有属性
    
    def __init__(self,name,age)"
        self.name = name
        self.age = age
    def say(self):      #公有方法
        print("my name is %s i have %d" % (self.name,self.__money))
    def __lie(self):        #私有方法
        print('i have 5000')

zhangsan = Human('zhangsan',30)
#zhangsan.name = 'zhangsan'
print(zhangsan.name)
zhangsan.say()
