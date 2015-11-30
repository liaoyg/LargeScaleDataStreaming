import cPickle as pickle
from math import *
from random import *
import scipy.misc

def Triangles():
    k = 8       ##number of machines
    filename = 'com-dblp.ungraph'
    order = 'bfs'
    #order = 'dfs'
    #order = 'rand'

    adList = pickle.load(open(filename+'.p','rb'))
    Stream = pickle.load(open(filename+'_'+order+'.p','rb'))
    print type(adList),type(Stream)
    print adList[3],adList[35]
    print "total nodes:",len(adList.keys()),len(Stream)

    print "Partition"

    Cap = len(Stream)/k + 1     ##Capacity of each machine
    curSelectedMach = 0         ##init the default selected machine number
    cutEdges = 0                ##number of edges being cut
    Machines = []               ##List of machines
    Machine = set()             ##Single machine
    for i in xrange(k):         ##init k sets
        Machine = set()         ##Single machine
        Machines.append(Machine)


    for curNode in Stream:
        ##find the machine that has most v's neighbor
        curNeighbors = adList[curNode]
        NeighborSets = []                   ##init neighbor set
        for i in xrange(k):
            NeighborSet = set()
            NeighborSets.append(NeighborSet)

        mostEdgeMach = [0]*k                ##How may neighbors in each machine
        for Neighbor in curNeighbors:
            if Neighbor == curNode:         ##Skip first node
                continue
            for i in xrange(k):
                if Neighbor in Machines[i]:  
                    NeighborSets[i].add(Neighbor)      ##add neighbors to corresponding neighbor set
                    mostEdgeMach[i] += 1
                    break
                else:
                    continue

        EdgesinEachSet = [0]*k
        for i in xrange(k):                             ##Iter all machines
            for j in NeighborSets[i]:                   ##Iter inside each neighborset
                tempNeighborList = adList[j]            ##get neighbor for each node in a neighbor set
                for otherNeighbor in NeighborSets[i]:   ##test if there exist edges between two nodes
                    if otherNeighbor == j:
                        continue
                    elif otherNeighbor in tempNeighborList:
                        EdgesinEachSet[i] += 1          ##count twice
            if EdgesinEachSet[i] == 0:                  ##if empty set
                continue
            EdgesinEachSet[i] /= 2
            choose2 = scipy.misc.comb(mostEdgeMach[i],2)
            EdgesinEachSet[i] /= int(choose2)

        ##Penalize larger partitions
        ##3 different ways to penalize
        for i in xrange(len(EdgesinEachSet)):
            #EdgesinEachSet[i] = EdgesinEachSet[i]
            EdgesinEachSet[i] = EdgesinEachSet[i] * (1 - (len(Machines[i]))/Cap)
            ##TODO FIX EXP
            EdgesinEachSet[i] = EdgesinEachSet[i] * (1 - exp(len(Machines[i])-Cap))


        #Argmax
        candidateMachList = [i for i,j in enumerate(EdgesinEachSet) if j == max(EdgesinEachSet)]
        if len(candidateMachList) == 1:                                 ##only one maximum edge machine, add to that machine
            curSelectedMach = candidateMachList[0]
            Machines[curSelectedMach].add(curNode)
        else:                                                           ##More than one machines has maximum edge, Randomly pick one
            randInd = randint(0,len(candidateMachList)-1)               ##Random pick one if ties
            curSelectedMach = randInd
            Machines[curSelectedMach].add(curNode)



        ##Calculate cutEdges
        for Neighbor in curNeighbors:
            if Neighbor == curNode:          ##Skip first node
                continue
            for i in xrange(k):
                if Neighbor in Machines[i] and i != curSelectedMach:    ##Neighbor was in a machine but not same as curNode
                    cutEdges += 1
                else:
                    continue

    print cutEdges
    total = 0
    for i in xrange(k):
        total += len(Machines[i])
        print i,len(Machines[i])
    print total


if __name__ == '__main__':
    Triangles()
