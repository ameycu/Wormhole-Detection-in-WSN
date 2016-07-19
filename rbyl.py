from Node import *
from Location import *
import pylab 

WORM_HOLE_LINK = 10

class attackernode2(node):
    def __init__(self, attacker, name):
        self.name = name
        self.rang = ATTACKER_NODE_RANGE
        self.loc = attacker.loc.getLoc(r.randrange(361), WORM_HOLE_LINK)
        field.addNode(self, self.loc)

a=attackernode('a1')
b=attackernode2(a, 'a2')
print 'b_x = ', b.loc.getx()
print 'b_y = ', b.loc.gety()
print 'dist between a and b = ', round(b.loc.distFrom(a.loc))
nodes=[a, b]

pylab.figure(1)
x = []
y = []
for node in nodes:
    x.append(node.loc.getx())
    y.append(node.loc.gety())
    
pylab.scatter(x, y, marker='o', c='b')

pylab.grid()
pylab.show()
