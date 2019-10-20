from collections import Iterable #导入迭代判断（Python3.8后弃用）
str = isinstance('abc',Iterable) #判断字符串是否可迭代
list1 = isinstance([1,2,3],Iterable) #判断列表是否可迭代
nuber1 = isinstance(123,Iterable) #判断数字是否可迭代
print(str,list1,nuber1)
print('#'*50)
for x,y in [(1,2),(3,4),(5,6)]:     #迭代列表
    print(x,y)
print('#'*50)
d = {'a':1,'b':2,'c':3}     #迭代字典键
for key in d:
    print(key)
print('#'*50)
for k,v in d.items():       #迭代字典键值对
    print(k,v)
print('#'*50)
ls = ['a','b','c']
for i,v in enumerate(ls):       #迭代列表索引和值
    print(i,v)
print('#'*50)