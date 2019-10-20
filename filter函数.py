''' #利用filter求质数序列
def old_list():
    n = 1
    while True:
        n += 2
        yield n 

def d(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = old_list()
    while True:
        n = next(it)
        yield n
        it = filter(d(n),it)

for i in primes():
    if i < 1000:
        print(i)
    else:
        break
'''

#利用filter求回数序列
def pan_duan(n):
    str1 = str(n)
    str2 = str1[::-1]
    return str1 == str2

outp = filter(pan_duan,range(1,1000))
print(list(outp))

