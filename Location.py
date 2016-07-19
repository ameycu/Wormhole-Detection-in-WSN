import math as m

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

    def getLoc(self, theta, radius):
        theta = m.pi*theta/180
        newX = self.getx() + round(radius*(m.cos(theta)),3)
        newY = self.gety() + round(radius*(m.sin(theta)),3)
        return Location(newX, newY)
    
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
