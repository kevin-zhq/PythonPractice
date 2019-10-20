l1 = [x*x for x in range(1,11)]      #创建一个list
g1 = (x*x for x in range(1,11))      #创建一个generator
print(l1)
print(g1)
#区别是[]和()
#generator调用一个元素后就不保存元素，保存的是算法，无调用时弹出StopIteration错误
print(next(g1))
print(next(g1))
print('#'*50)
for i in g1:
    print(i)
print('#'*50)
# print(next(g1))     #一般不用nest()调用generator元素

#斐波那契数列,yield生成器
def fib(max):
    n,a,b = 0,0,1
    #l1 = []
    while n < max:
        yield b # l1.append(b)
        a,b = b,a+b
        n += 1
    return('完成')
#迭代、
print(fib(6))
for i in fib(6):
    print(i)
