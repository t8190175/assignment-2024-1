import sys

def print_tromino(n,p):
    for i in range(2 ** n):
        for j in range(2 ** n):
            if j < 2 ** n - 1:
                print(p[i][j], end=' ')
            else:
                print(p[i][j], end='\n')


def create_tromino(n, p):
    if n==1:
        p[0][0] = 'G'
        p[0][1] = 'X'
        p[1][0] = 'G'
        p[1][1] = 'G'
        return p
    if n==2:

        p[1][1] = 'G'
        p[1][2] = 'G'
        p[2][1] = 'G'

        p[2][2] = 'B'
        p[2][3] = 'B'
        p[3][2] = 'B'

        p[0][0] = 'B'
        p[0][1] = 'B'
        p[1][0] = 'B'

        p[2][0] = 'R'
        p[3][0] = 'R'
        p[3][1] = 'R'

        p[0][2] = 'R'
        p[0][3] = 'R'
        p[1][3] = 'R'

        return p



try:
    n = int(sys.argv[1])
except:
    print('Program must be run followed by integer argument n, where n > 1')
    exit()

if (n<1):
    print('Program must be run followed by integer argument n, where n > 1')
    exit()

p=[]
for i in range(2**n):
    row = []
    for j in range(2**n):
        row.append('X')
    p.append(row)


p = create_tromino(n, p)
print_tromino(n,p)
