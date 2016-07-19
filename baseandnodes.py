import random
import pylab
axes = pylab.axes()

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
    
    def getx(self):
        return self.x
    
    def gety(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

class Field(object):
    def __init__(self):
        self.nodes = {}

    def addNode(self, node, loc):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes[node] = loc

field = Field()

RANGE = 10

class node():
    def __init__(self, name):
        self.name = name
        self.location = Location(random.randrange(-RANGE,RANGE+1),random.randrange(-RANGE,RANGE+1))
        field.addNode(name, self.location)
        
    def setLinks(self):
        self.links = []
        for node in field.nodes.keys():
            distance = self.location.distFrom(field.nodes[node])
            if ((distance != 0)and(distance < self.rang)):
                self.links.append(node)

    def getLinks(self):
        return self.links

    def __str__(self):
        return self.name

class normalnode(node):
    def __init__(self, name):
        self.rang = 5
        node.__init__(self, name)

class attackernode(node):
    def __init__(self, name):
        self.rang = 10
        node.__init__(self, name)

class basestation(node):
    def __init__(self):
        self.rang = 20
        self.location = Location(0,0)
        field.addNode('base', self.location)


normal_nodes = 10
attacker_nodes = 2

nodes = []
for i in range(normal_nodes):
    nodes.append(normalnode(str(i)))

for i in range(normal_nodes + 1, normal_nodes + attacker_nodes + 1):
    nodes.append(attackernode(str(i)))

base = basestation()

for node in nodes:
    node.setLinks()
    print node,node.location,' Links: ',node.getLinks()

base.setLinks()
print 'Base Links: ',base.getLinks(),' ',len(base.getLinks()) 

x = []
y = []
for node in nodes:
    x.append(node.location.getx())
    y.append(node.location.gety())


pylab.figure(1) #Node distribution with links
pylab.xlim([-25,25])
pylab.ylim([-20,20])
pylab.title('Node distribution with links')
pylab.scatter(x[:normal_nodes+1], y[:normal_nodes+1], marker='o', c='b')
pylab.scatter(x[normal_nodes:], y[normal_nodes:], marker='o', c='r')
pylab.scatter([base.location.getx()], [base.location.gety()], marker='*', c='y')
circle_base = pylab.Circle((0,0), radius=0.1, color='y')
axes.add_patch(circle_base)

for i in range(len(x)):
    if i >= normal_nodes:
        circle = pylab.Circle((x[i], y[i]), radius=10, color='r',fill=False)
        axes.add_patch(circle)

pylab.grid()

for node1 in nodes:
    for node2 in nodes:
        if str(node2) in node1.getLinks():
            pylab.plot((node1.location.getx(),node2.location.getx()),(node1.location.gety(),node2.location.gety()),'g-')

pylab.show()








