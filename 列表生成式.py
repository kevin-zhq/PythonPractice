#列表生成式
l1 = list(range(1,11)) #简单的顺序列表生成
print(l1)

#稍复杂列表[1*1,2*2,....10*10]
l2 = []
for i in range(1,11):
    l2.append(i*i)
print(l2)

#更简洁的代码---Python 真正的列表生成式
l3 = [i*i for i in range(1,11)]     #i*i 需要写在最前面，后跟for循环，然后还可以加if判断
print(l3)

#偶数的平方
l4 = [i*i for i in range(1,11) if i % 2 == 0]
print(l4)


#两层循环
l5 = [x+y for x in l2 for y in l3]
print(l5)

#列出当前目录下文件名
'''
import os     #导入os模块
l6 = [d for d in os.listdir('.')] #os.listdir可列出文件和目录
print(l6)
'''

#大小写转换
l7 = ['hello','world',18,'Apple',None]      #数字没有大小写转换，会报错，所以要做处理
l8 = [s.capitalize() for s in l7 if isinstance(s,str)]
l9 = [s.lower() for s in l7 if isinstance(s,str)]
print(l8,'\n',l9)