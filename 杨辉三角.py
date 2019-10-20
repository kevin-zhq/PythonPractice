#杨辉三角问题
def yanghui():
    line = [1]
    while True:
        yield line
        line = [1]+[line[i]+line[i+1] for i in range(len(line)-1)]+[1]

def triangle(row):
    n = 0
    for i in yanghui():
        n += 1
        print(i)
        if n == row:
            break

triangle(3)