import pylab
from Node import *
from Location import *

axes = pylab.axes()

x_lim = RANGE*2 + 5
y_lim = RANGE*2

def RedCircle(center, rad):
    axes = pylab.axes()
    circle = pylab.Circle((center.getx(), center.gety()), radius=rad, color='r',fill=False)
    axes.add_patch(circle)
    

def PlotNodeDistribution(normal_nodes, attacker_nodes, base, naming = True):
    pylab.figure(1)
    pylab.xlim([-x_lim,x_lim])
    pylab.ylim([-y_lim,y_lim])
    pylab.title('Node distribution')
    x = []
    y = []
    for node in normal_nodes:
        if naming:
            pylab.text(node.loc.getx(), node.loc.gety() - 1.5, str(node))
        x.append(node.loc.getx())
        y.append(node.loc.gety())
    pylab.scatter(x, y, marker='o', c='b')
    

    x_a = []
    y_a = []
    for node in attacker_nodes:
        if naming:
            pylab.text(node.loc.getx() - 1.5, node.loc.gety() - 1.5, str(node))
        x_a.append(node.loc.getx())
        y_a.append(node.loc.gety())
        RedCircle(node.loc, ATTACKER_NODE_RANGE)
    pylab.scatter(x_a, y_a, marker='o', c='r')

    pylab.scatter([base.loc.getx()], [base.loc.gety()], marker='o', c='y')
    if naming:
        pylab.text(base.loc.getx() - 1.5, base.loc.gety() - 1.5, str(base))

    pylab.grid()
    pylab.show()

def PlotNodeLinks(normal_nodes, attacker_nodes, base, naming = False):
    pylab.figure(2)
    pylab.xlim([-x_lim,x_lim])
    pylab.ylim([-y_lim,y_lim])
    pylab.title('Node Links')
    x = []
    y = []
    for node in normal_nodes:
        if naming:
            pylab.text(node.loc.getx(), node.loc.gety() - 1.5, str(node))
        x.append(node.loc.getx())
        y.append(node.loc.gety())
    pylab.scatter(x, y, marker='o', c='b')

    x_a = []
    y_a = []
    for node in attacker_nodes:
        if naming:
            pylab.text(node.loc.getx() - 1.5, node.loc.gety() - 1.5, str(node))
        x_a.append(node.loc.getx())
        y_a.append(node.loc.gety())
        RedCircle(node.loc, ATTACKER_NODE_RANGE)
    pylab.scatter(x_a, y_a, marker='o', c='r')

    pylab.scatter([base.loc.getx()], [base.loc.gety()], marker='o', c='y')
    if naming:
        pylab.text(base.loc.getx() - 1.5, base.loc.gety() - 1.5, str(base))

    pylab.grid()
    
    nodes = normal_nodes + attacker_nodes
    nodes.append(base)
    for node1 in nodes:
        for node2 in nodes:
            if node2 in node1.getLinks():
                pylab.plot((node1.loc.getx(),node2.loc.getx()),(node1.loc.gety(),node2.loc.gety()),'g-')

    for node1 in attacker_nodes:
        for node2 in attacker_nodes:
            if node2 != node1:
                pylab.plot((node1.loc.getx(),node2.loc.getx()),(node1.loc.gety(),node2.loc.gety()),'r-')
                

    
    pylab.show()











    
        
