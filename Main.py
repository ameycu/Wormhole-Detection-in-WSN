from Node import *
from Location import *
from Graphics import *

#Constatns
NORMAL_NODES = 10 #Number of Normal Nodes
ATTACKER_NODES = 2 #Number of Attacker Nodes

normal_nodes = []
for i in range(NORMAL_NODES):
    normal_nodes.append(normalnode(str(i)))

attacker_nodes = []
for i in range(ATTACKER_NODES):
    attacker_nodes.append(attackernode('atck'+str(i)))

nodes = normal_nodes + attacker_nodes

base = basestation()

nodes.append(base)

PlotNodeDistribution(normal_nodes, attacker_nodes, base)

setLinks()

PlotNodeLinks(normal_nodes, attacker_nodes, base)


Localized = True
for attacker in attacker_nodes:
    for attacker_link in attacker.getLinks():
        if (attacker_link in normal_nodes) or (attacker_link == base):
            Localized = False
            break

print 'Base Links: ',base.getLinksnames(),' ',len(base.getLinksnames())
for node in nodes:
   print node,node.loc,' Links: ',node.getLinksnames()

if Localized:
    print 'LOCALIZED'
else:
    print 'NOT LOCALIZED'
