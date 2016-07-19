import random as r
import math as m
from Location import *


# CONSTANTS
RANGE = 100 # Range over which nodes will be distributed
NORMAL_NODE_RANGE = 5
ATTACKER_NODE_RANGE = 10
BASE_STATION_RANGE = 5

field = Field()

class node():
    def __init__(self, name):
        self.name = name
        self.loc = Location(r.randrange(-RANGE,RANGE+1),r.randrange(-RANGE,RANGE+1))
        field.addNode(self, self.loc)

    def getLinks(self):
        return self.links

    def getLinksnames(self):
        Links_names = []
        for link in self.links:
            Links_names.append(link.name)
        Links_names.sort()
        return Links_names

    def __str__(self):
        return self.name

class normalnode(node):
    def __init__(self, name):
        self.rang = NORMAL_NODE_RANGE
        node.__init__(self, name)

class attackernode(node):
    def __init__(self, name):
        self.rang = ATTACKER_NODE_RANGE
        node.__init__(self, name)
        
class basestation(node):
    def __init__(self):
        self.name = 'Base'
        self.rang = BASE_STATION_RANGE
        self.loc = Location(0,0)
        field.addNode(self, self.loc)


def setLinks():
    for node1 in field.nodes.keys():
        node1.links=[]
        for node in field.nodes.keys():
            distance = node1.loc.distFrom(field.nodes[node])
            if ((distance != 0)and(distance < max(node1.rang,node.rang))):
                node1.links.append(node)
                
    
