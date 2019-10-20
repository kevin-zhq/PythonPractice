

def hanoi(n,a,b,c):
    if n==1:
        print('%s-->%s' % (a,c))
    else:
        hanoi(n-1,a,c,b)
        hanoi(1,a,b,c)
        hanoi(n-1,b,a,c)


#use
#hanoi(3,'A','B','C')    # hanoi(2,'A','C','B') # hanoi(1,'A','B','C') # A--C
                                               # A--B
                                               # hanoi(1,'C','A','B') # C--B
                        # A--C 
                        # hanoi(2,'B','A','C') # hanoi(1,'B','C','A') # B--A
                                               # B--C
                                               # hanoi(1,'A','B','C') # A--C
hanoi(2,'A','B','C')

