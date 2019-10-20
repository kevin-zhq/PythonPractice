#sorted函数
l1 = [36,5,-12,9,-21]
l2 = ['bob','about','Zoo','Credit']

l3 = sorted(l1) #返回另一个序列，而非原序列更改
print(l1)
print('按照从小到大排序',l3)

l4 = sorted(l1,key=abs)
print('按照绝对值从小到大排序',l4)

l5 = sorted(l2)
print('按照ASCII从小到大排序',l2)
print(l5)

l6 = sorted(l2,key=str.lower)
print('按照ASCII小写字幕从小到大排序',l6)

l7 = sorted(l2,key=str.lower,reverse=True)
print('按照ASCII小写字幕大小排序，从大到小',l7)


#练习
l8 = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

#按照名字排序
def by_name(t):
    return t[0]

#按照分数排序
def by_score(t):
    return t[1]

print(sorted(l8,key=by_name))
print(sorted(l8,key=by_score))

