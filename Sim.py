from Node import *
from Location import *

#Constatns
NORMAL_NODES = 10 #Number of Normal Nodes
ATTACKER_NODES = 2 #Number of Attacker Nodes
NUM_TRIALS = 50

Count = 0

for trial in range(NUM_TRIALS):
    
    normal_nodes = []
    for i in range(NORMAL_NODES):
        normal_nodes.append(normalnode(str(i)))

    attacker_nodes = []
    for i in range(ATTACKER_NODES):
        attacker_nodes.append(attackernode('atck'+str(i)))

    #nodes = normal_nodes + attacker_nodes

    base = basestation()

    #nodes.append(base)

    setLinks()

    Localized = True
    for attacker in attacker_nodes:
        for attacker_link in attacker.getLinks():
            if (attacker_link in normal_nodes) or (attacker_link == base):
                Localized = False
                break

    if Localized:
        Count += 1

PROBABILITY = float(Count)/NUM_TRIALS
print 'Probability of Localization: ',PROBABILITY
