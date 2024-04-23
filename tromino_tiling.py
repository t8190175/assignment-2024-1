import sys

n = int(sys.argv[1])
if (n<1):
    print('Program must be run followed by integer argument n, where n > 1)
    return

p={}
p[(1,1)] = 'B'
p[(1,2)] = 'B'
p[(1,3)] = 'R'
p[(1,4)] = 'R'
p[(2,1)] = 'B'
p[(2,2)] = 'G'
p[(2,3)] = 'G'
p[(2,4)] = 'R'
p[(3,1)] = 'R'
p[(3,2)] = 'G'
p[(3,3)] = 'B'
p[(3,4)] = 'B'
p[(4,1)] = 'R'
p[(4,2)] = 'R'
p[(4,3)] = 'B'
p[(4,4)] = 'X'


for k, v in p.items():
    pos = k
    r=k[0]
    c=k[1]
    if c!=4:
        print(v, end=' ')
    else:
        print(v, end='\n')

##B B R R
##B G G R
##R G B B
##R R B X

n=input('n=')
def create_tromino(n):
      p={}
      if n==1:
            p[(1,1)] = 'G'
            p[(1,2)] = 'X'
            p[(2,1)] = 'G'
            p[(2,2)] = 'G'
            return p
      if n==2:
            
            
