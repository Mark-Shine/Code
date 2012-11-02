def add(x,y): return x+y
print reduce(add,range(1,11))

def f(x): return x%2 != 0 and x%3 != 0
print filter(f,range(2,25))

def cube(x): return x*x*x
print map(cube, range(1, 11))

seq = range(8)
def add(x, y): return x+y
print map(add, seq, seq)
