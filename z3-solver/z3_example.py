from z3 import *

# find the variable that made true di expression: x & y & (x ^ z)

# define vars and solver
x = BitVec("x", 1)
y = BitVec("y", 1)
z = BitVec("z", 1)
s = Solver()

# constrains
s.add((x & y & (x ^ z)) == 1)

if s.check() == sat:
    m = s.model()
    print(m)
