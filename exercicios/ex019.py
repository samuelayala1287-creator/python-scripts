n = int(input('VocÊ quer saber a tabueada de qual número? '))

for t in range (0, 10):
    multi = n * t
    print('{} x {} = {}'.format(n, t, multi))